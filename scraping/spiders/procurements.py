# -*- coding: utf-8 -*-
import urllib
from urlparse import urljoin
import scrapy
from scrapy import http, log

from scraping.items import PublicProcurementItem, BidderCompanyItem, ContractingAuthorityItem


class PublicProcurementSpider(scrapy.Spider):
    name = "procurements"
    allowed_domains = ["portal.ujn.gov.me"]

    BASE_URL = "http://portal.ujn.gov.me"
    LOGIN_URL = urljoin(BASE_URL, "/delta/j_security_check")
    SEARCH_URL = urljoin(BASE_URL, "/delta/search/noticeSearch.html")
    SEARCH_RESULTS_URL = urljoin(BASE_URL, "/delta/search/noticeSearchResults.html")
    DETAIL_PAGE_URL = urljoin(BASE_URL, "/delta/search/displayNotice.html")

    USER_AGENT = "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"

    USERNAME = "veritzateam"
    PASSWORD = "veritzateam2014"

    START_DATE = "01/01/2009"
    END_DATE = "31/12/2019"

    start_urls = [
        BASE_URL
    ]

    HEADERS = {
        "Origin": "http://portal.ujn.gov.me",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://portal.ujn.gov.me/delta/search/noticeSearch.html",
    }

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'j_username': self.USERNAME, 'j_password': self.PASSWORD, 'login': 'Ulogujte se'},
            callback=self.after_logged_in
        )

    def after_logged_in(self, response):
        # decision on award request
        # yield http.Request(url=self.SEARCH_URL, method='POST',
        #                    body=urllib.urlencode({
        #                        'title': '', 'advanced': 1, 'noticeType': 'DecisionOnAward',
        #                        'startDate': self.START_DATE, 'endDate': self.END_DATE
        #                    }), headers=self.HEADERS, callback=self.parse_data, dont_filter=True)

        # contract of award request
        yield http.Request(url=self.SEARCH_URL, method='POST',
                           body=urllib.urlencode({
                               'title': '', 'advanced': 1, 'noticeType': 'ShoppingDecision',  # Contract of Award
                               'startDate': self.START_DATE, 'endDate': self.END_DATE,
                           }), headers=self.HEADERS, callback=self.parse_data, dont_filter=True)

    def parse_data(self, response):
        page_count = int(response.xpath('//span[@class="pagelinks"]/a[last()]/@href')[0].extract().lstrip('?page='))
        page_count = page_count or 0
        log.msg("page_count: %s" % page_count, level=log.ERROR)
        for page_num in xrange(1, page_count + 1):
            yield http.Request(url="{0}?{1}".format(self.SEARCH_RESULTS_URL,
                                                    urllib.urlencode({'page': page_num})),
                               callback=self.parse_public_procurement)

    def parse_public_procurement(self, response):
        for row in response.xpath('//table[@id="noticeList"]//tr')[1:]:
            procurement = PublicProcurementItem()
            procurement_id = ''.join(row.xpath('td[6]/input[@type="button"]/@onclick')[0].re('id=(\d+)'))
            procurement.update({
                'system_id': procurement_id,
                # 'buyer': ''.join(row.xpath('td[1]/text()').extract()).strip(),
                'title': ''.join(row.xpath('td[2]/text()').extract()).strip(),
                'description': ''.join(row.xpath('td[3]/text()').extract()).strip(),
                'record_type': ''.join(row.xpath('td[4]/text()').extract()).strip(),
                'creation_date': ''.join(row.xpath('td[5]/text()').extract()).strip(),
                'link': "{0}?id={1}".format(self.DETAIL_PAGE_URL, procurement_id)
            })

            yield http.Request(url=procurement['link'],
                               meta={'procurement': procurement},
                               callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        procurement = response.meta['procurement']

        # Collect common data
        contracting_authority_name, number, location_date = response.xpath('//table[@class="notice-header"]/following-sibling::div[1]/p/strong/text()').extract()
        location = location_date.rsplit(' ', 1)[0]
        contracting_authority = ContractingAuthorityItem()
        contracting_authority['name'] = contracting_authority_name.strip()

        procurement.update({
            'number': number.strip(),
            'location': location.strip(),
            'subject': ''.join(response.xpath('//div[@class="container"]/fieldset[4]/div/form/p/input[@type="radio"][@checked="checked"]/@value').extract()).strip(),
        })

        # Collect ContractingAuthority data
        table = response.xpath('//div[@class="container"]/fieldset[2]/table/tbody')
        if table:
            table = table[0]

            contracting_authority.update({
                'procurement_number': procurement['number'],
                'identification_number': ''.join(table.xpath('tr[3]/td[2]/strong/text()').extract()).strip(),
                # 'contact_person': ''.join(table.xpath('tr[1]/td[2]/strong/text()').extract()).strip(),
                'address': ''.join(table.xpath('tr[2]/td[1]/strong/text()').extract()).strip(),
                'town': ''.join(table.xpath('tr[3]/td[1]/strong/text()').extract()).strip(),
                'email': ''.join(table.xpath('tr[5]/td[1]/strong/text()').extract()).strip(),
                'webpage': urljoin('http://', ''.join(table.xpath('tr[5]/td[2]/strong/text()').extract()).strip()),
            })

        yield contracting_authority

        # Collect BidderCompany data
        bidder = BidderCompanyItem()

        if procurement['record_type'] == "Contract of award":
            bidder_table = response.xpath('//div[@class="container"]/fieldset[6]/table')
            try: procurement['value'] = ''.join(response.xpath('//fieldset[5]/p/strong/text()')[0].re(ur'([\d\.])')).strip()
            except IndexError: pass

        elif procurement['record_type'] == "Decision on Award":
            bidder_table = response.xpath('//div[@class="container"]/fieldset[11]/table')
            try: procurement['value'] = ''.join(response.xpath('//fieldset[6]/p/text()')[0].re(ur'([\d\.])')).strip()
            except IndexError: pass
        else:
            return

        if bidder_table:
            bidder_table = bidder_table[0]
            bidder.update({
                'procurement_number': procurement['number'],
                'name': ''.join(bidder_table.xpath('tr[1]/td[1]/text()').extract()).strip(),
                'identification_number': ''.join(bidder_table.xpath('tr[3]/td[2]/text()').extract()).strip(),
                'contact_point': ''.join(bidder_table.xpath('tr[1]/td[2]/text()').extract()).strip(),
                'postal_address': ''.join(bidder_table.xpath('tr[2]/td[1]/text()').extract()).strip(),
                'town': ''.join(bidder_table.xpath('tr[3]/td[1]/text()').extract()).strip(),
                'email': ''.join(bidder_table.xpath('tr[5]/td[1]/text()').extract()).strip(),
                'webpage': ''.join(bidder_table.xpath('tr[5]/td[2]/text()').extract()).strip(),
            })

            yield bidder

        yield procurement
