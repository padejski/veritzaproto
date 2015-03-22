# -*- coding: utf-8 -*-
import math
import urllib
import urlparse
import logging
import scrapy
from scrapy import http


from scraping.items import CompanyItem, CompanyMemberItem, CompanyMemberTitleItem

L = logging.getLogger('debug')

class CompaniesSpider(scrapy.Spider):
    name = "companies"
    allowed_domains = ["www.crps.me"]

    BASE_URL = "http://www.crps.me/CRPSPublic/"
    SEARCH_URL = urlparse.urljoin(BASE_URL, "rezultatpretrageregistra.action")
    DETAIL_PAGE_URL = urlparse.urljoin(BASE_URL, "prikazidrustvo.action")

    RESULTS_PER_PAGE = 15

    DEFAULT_PARAMS = {
        "od": 1,
        "privrednaDjelatnost": 0,
        "naziv": "",
        "opstina": 0,
        "lice": "",
        "djelatnostId": "",
        "sortiranje": 1,
        "regBr": "",
        "prikazati": 0,
    }

    PRIVREDNA_DJELATNOST_CHOICES = {
       'SVE': 0,
       'PREDUZETNIK': 1,
       'ORTAČKO DRUŠTVO': 2,
       'KOMANDITNO DRUŠTVO': 3,
       'AKCIONARSKO DRUŠTVO': 4,
       'DRUŠTVO SA OGRANIČENOM ODGOVORNOŠĆU': 5,
       'DIO STRANOG DRUŠTVA': 6,
       'NEVLADINA ORGANIZACIJA': 7,
       'USTANOVA': 8,
       'USTANOVA': 9,
       'OSTALI OBLICI OBAVLJANJA PRIVREDNE DJELATNOSTI': 10,
       'INVESTICIONI FONDOVI': 11,
    }

    PRIVREDNA_DJELATNOST_CHOICES_REVERSE = {
        0: 'SVE',
        1: 'PREDUZETNIK ( P )',
        2: 'ORTAČKO DRUŠTVO ( O.D. )',
        3: 'KOMANDITNO DRUŠTVO ( KD )',
        4: 'AKCIONARSKO DRUŠTVO ( AD )',
        5: 'DRUŠTVO SA OGRANIČENOM ODGOVORNOŠĆU ( DOO )',
        6: 'DIO STRANOG DRUŠTVA ( DSD )',
        7: 'NEVLADINA ORGANIZACIJA ( NVO )',
        8: 'USTANOVA ( UST )',
        9: 'USTANOVA ( UST )',
        10: 'OSTALI OBLICI OBAVLJANJA PRIVREDNE DJELATNOSTI ( OST )',
        11: 'INVESTICIONI FONDOVI ( FOND )',
    }


    DEFAULT_PARAMS_ENCODED = urllib.urlencode(DEFAULT_PARAMS)

    start_urls = [
        "{0}?{1}".format(SEARCH_URL, DEFAULT_PARAMS_ENCODED),
    ]

    def parse(self, response):
        # get total records count to calculate number of pages of results
        total_records_count = int(''.join(response.xpath('//div[@class="prozorpodaci"]/text()')
                                    .re("\( Zapisi \d+ - \d+ / (\d+) \)"))) or 1

        # calculate the page count given the results per page
        page_count = int(math.floor(total_records_count / float(self.RESULTS_PER_PAGE)))

        # loop over each results page
        for page_num in xrange(0, page_count + 1):
            params_encoded = self.DEFAULT_PARAMS.copy()
            params_encoded.update({'od': page_num * self.RESULTS_PER_PAGE + 1})
            params_encoded = urllib.urlencode(params_encoded)

            # fetch and parse the next page
            yield http.Request(url="{0}?{1}".format(self.SEARCH_URL, params_encoded), callback=self.collect_rows)

    def collect_rows(self, response):
        company = CompanyItem()
        try:
            table = response.xpath('//div[@class="prozorpodaci"]/table')[0]
            columns = map(self.normalize_column_name, table.xpath('tr[@class ="naslov"]/td/text()').extract())  # + ['lat', 'lng']

            # loop over results and get some basic company info
            for row in table.xpath('tr')[1:]:
                fields = []
                for cell in row.xpath('td')[:-2]:  # last two cells contain buttons, not data
                    fields.append(cell.xpath('text()')[0].extract().strip())
                company = CompanyItem.from_dict(dict(zip(columns, fields)))

                # We need company ID to construct company's detail page.
                # We also set the company's url here (called 'link')
                id_dosijea = ''.join(row.xpath('td[8]/form/input[@type="hidden"]/@value').extract())
                url = "{0}?{1}".format(self.DETAIL_PAGE_URL, urllib.urlencode({"idDosijea": id_dosijea}))
                company.update({'link': url})

                # fetch and parse company detail page
                yield http.Request(url=url, meta={'company': company}, callback=self.parse_detail_page)

        except IndexError as e:
            print(e)

    def normalize_column_name(self, name):
        return name.lower().replace(' ', '_')

    def parse_detail_page(self, response):
        """
        Parse company info from company's detail page. Then parse company members data.
        """
        company = response.meta['company']

        company.update({
            'full_name': ''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Puni naziv")]/following-sibling::text()[1]').extract()).strip(),
            'address': "%s, %s" % (''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Adresa sjedi")]/following-sibling::text()[1]').extract()).strip(),
                                    ''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Mjesto sjedi")]/following-sibling::text()[1]').extract()).strip()),
            'mail_address': "%s, %s" % (''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Adresa prijema slu")]/following-sibling::text()[1]').extract()).strip(),
                                    ''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Mjesto prijema slu")]/following-sibling::text()[1]').extract()).strip()),
            'registration_date': ''.join(response.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Datum registracije")]/following-sibling::text()[1]').extract()).strip(),
        })

        # Pass company data to the pipeline so it can be stored. Company record must be stored
        # in the database before CompanyMember record because the latter has ForeignKey to the former.
        yield company

        # parse company members data
        for company_member in self.parse_members(response):
            yield company_member

    # This is not a callback!
    def parse_members(self, response):
        """
        Parses 'Lica u drustvu' tab on the company detail page
        """
        company = response.meta['company']
        members = []
        member_titles = []
        member = CompanyMemberItem()
        member_title = CompanyMemberTitleItem()

        elements = response.xpath('//div[@class="tabbertab"][2]/span | //div[@class="tabbertab"][2]/table')
        for element in elements:
            if element.extract().strip().startswith('<span'):
                if member:
                    # we reached next member, add current one to the collection and start collecting the next one
                    member.update({
                        'company_registration_number': company.get('registration_number', ""),
                        'link': company['link'],
                    })
                    member_title.update({
                        'company_registration_number': company.get('registration_number', ""),
                    })
                    members.append(member)
                    member = CompanyMemberItem()
                    member_title = CompanyMemberTitleItem()
                    member_title.update({
                        'title': ''.join(element.xpath('b/text()').extract()).strip(),
                    })
            elif element.extract().strip().startswith('<table'):
                key = ''.join(element.xpath('descendant::td[1]/b/text()').extract()).strip().lower().replace(':', '').strip()
                value = ''.join(element.xpath('descendant::td[2]/text()').extract()).strip()
                if key in (u'ime', 'ime'):
                    key = u'first_name'
                elif key in (u'prezime', 'ime'):
                    key = u'last_name'
                elif key in (u'odgovornost', 'odgovornost'):
                    member_title['title'] = value
                elif key in (u'Udio u društvu'):
                    member_title['company_share'] = value

                if key in CompanyMemberItem.fields.keys():
                    member[key] = value

        # add the last member, obviously there won't be <span> element at the and to designate member data end
        member.update({
            'company_registration_number': company.get('registration_number', ""),
            'link': company['link'],
        })
        member_title['company_registration_number'] = company.get('registration_number', "")

        members.append(member)
        member_titles.append(member_title)

        # Pass parsed members to the pipeline so they are stored
        return members
