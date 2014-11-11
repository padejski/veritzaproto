#!/usr/bin/env python
import re
import time
from urlparse import urljoin
import lxml.html
import requests

from django.conf import settings

from veritza.apps.core.models import PublicProcurement

BASE_URL = "http://portal.ujn.gov.me"
LOGIN_URL = urljoin(BASE_URL, "/delta/j_security_check")
SEARCH_URL = urljoin(BASE_URL, "/delta/search/noticeSearch.html")
SEARCH_RESULTS_URL = urljoin(BASE_URL, "/delta/search/noticeSearchResults.html")
DETAIL_PAGE_URL = urljoin(BASE_URL, "/delta/search/displayNotice.html")

USER_AGENT = "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"

USERNAME = "veritzateam"
PASSWORD = "veritzateam2014"


class PublicProcurementScraper(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENT})
        self.auth_data = {'j_username': USERNAME, 'j_password': PASSWORD, 'login': 'Ulogujte se'}
        self.login()

    def login(self):
        r = self.session.post(LOGIN_URL, data=self.auth_data)
        # print(r.text, r.reason, r.status_code, r.headers, dir(r))

    def get(self, *args, **kwargs):
        return lxml.html.fromstring(self.session.get(*args, **kwargs).content)

    def post(self, *args, **kwargs):
        return lxml.html.fromstring(self.session.post(*args, **kwargs).content)

    def get_page_count(self, html):
        return int(html.xpath('//span[@class="pagelinks"]/a[last()]/@href')[0].lstrip('?page='))

    def search(self, query_params):
        return self.post(SEARCH_URL, data=query_params)

    def parse_plan_public_procurement(self, html):
        return {}

    def parse_negotiate_invitation(self, html):
        return {}

    def parse_contract_award(self, html):
        data = self.parse_bidder_data(html, '//div[@class="container"]/fieldset[6]/table')
        data.update(self.parse_procurement_value(html, '//fieldset[5]/p/strong/text()'))
        return data

    def parse_decision_award(self, html):
        data = self.parse_bidder_data(html, '//div[@class="container"]/fieldset[11]/table')
        data.update(self.parse_procurement_value(html, '//fieldset[6]/p/text()'))
        data.update({'bids_number': self.re('were\s+submitted\s+by\s+(\d+)', ''.join(html.xpath('//div[@class="container"]/fieldset[10]/fieldset[1]/p//text()'))), })
        return data

    def parse_invitation_public_procurement(self, html):
        return self.parse_procurement_value(html, '//fieldset[6]/p/text()')

    def parse_decision_cancelling_tender(self, html):
        return self.parse_procurement_value(html, '//fieldset[6]/p/text()')

    def parse_shopping_method_invitation(self, html):
        return self.parse_procurement_value(html, '//fieldset[7]/p/text()')

    def parse_procurement_value(self, html, selector):
        return {'price': self.re('(\d+)', ''.join(html.xpath(selector)).strip())}

    def parse_bidder_data(self, html, selector):
        data = {}
        bidder_table = html.xpath(selector)
        if bidder_table:
            bidder_table = bidder_table[0]
            data.update({
                'bidder_name': ''.join(bidder_table.xpath('tr[1]/td[1]/text()')).strip(),
                'bidder_id': ''.join(bidder_table.xpath('tr[3]/td[2]/text()')).strip(),
                'bidder_contact_point': ''.join(bidder_table.xpath('tr[1]/td[2]/text()')).strip(),
                'bidder_postal_address': ''.join(bidder_table.xpath('tr[2]/td[1]/text()')).strip(),
                'bidder_town': ''.join(bidder_table.xpath('tr[3]/td[1]/text()')).strip(),
                'bidder_email': ''.join(bidder_table.xpath('tr[5]/td[1]/text()')).strip(),
                'bidder_webpage': ''.join(bidder_table.xpath('tr[5]/td[2]/text()')).strip(),
            })
        return data

    def parse_detail_page(self, html, notice_type):
        # Collect common data
        contracting_authority, number, place_date = html.xpath('//table[@class="notice-header"]/following-sibling::div[1]/p/strong/text()')
        data = {
            'contracting_authority': contracting_authority.strip(),
            'number': number.strip(),
            'place_date': place_date.strip(),
            'subject': ''.join(html.xpath('//div[@class="container"]/fieldset[4]/div/form/p/input[@type="radio"][@checked="checked"]/@value')).strip(),
        }

        if notice_type == 'Plan for Public Procurement':
            return data

        parsers = {
            'Decision on Award': self.parse_decision_award,
            'Invitation to Public Procurement': self.parse_invitation_public_procurement,
            'Shopping Method Invitation': self.parse_shopping_method_invitation,
            'Contract of award': self.parse_contract_award,
            'Decision on Cancelling a Tender': self.parse_decision_cancelling_tender,
            'Negotiate Invitation With Public Procure': self.parse_negotiate_invitation,
            #'Plan for Public Procurement': self.parse_plan_public_procurement,
        }

        # Collect Contracting Authority data
        table = html.xpath('//div[@class="container"]/fieldset[2]/table/tbody')
        if table:
            table = table[0]

            data.update({
                'identification_number': ''.join(table.xpath('tr[3]/td[2]/strong/text()')).strip(),
                'contact_person': ''.join(table.xpath('tr[1]/td[2]/strong/text()')).strip(),
                'address': ''.join(table.xpath('tr[2]/td[1]/strong/text()')).strip(),
                'town': ''.join(table.xpath('tr[3]/td[1]/strong/text()')).strip(),
                'webpage': urljoin('http://', ''.join(table.xpath('tr[5]/td[2]/strong/text()')).strip()),
                'bids_number': '',
            })

        # Collect public procurement data
        data.update(parsers[notice_type](html))

        return data

    def parse_data(self, html):
        rows = []
        for row in html.xpath('//table[@id="noticeList"]//tr')[1:]:
            record_id = self.re('id=(\d+)', row.xpath('td[6]/input[@type="button"]/@onclick')[0])
            record = {
                'id': record_id,
                'buyer': ''.join(row.xpath('td[1]/text()')).strip(),
                'title': ''.join(row.xpath('td[2]/text()')).strip(),
                'description': ''.join(row.xpath('td[3]/text()')).strip(),
                'notice_type': ''.join(row.xpath('td[4]/text()')).strip(),
                'creation_date': ''.join(row.xpath('td[5]/text()')).strip(),
                'link': DETAIL_PAGE_URL + '?id=' + record_id,
            }
            details_data = self.parse_detail_page(self.get(DETAIL_PAGE_URL, params={'id': record_id}), record['notice_type'])
            record.update(details_data)
            rows.append(record)
        return rows

    def re(self, pattern, text):
        match = re.search(pattern, text)
        if match and match.groups():
            return match.groups()[0]
        return ""

    def run(self, start_page=0, end_page=None):
        # we put empty title to get all results
        search_results = self.search({'title': '', 'startDate': '01/01/2013', 'endDate': '16/04/2014'})
        page_count = self.get_page_count(search_results)
        page_count = end_page or page_count
        for page_num in xrange(start_page + 1, page_count + 1):
            html = self.get(SEARCH_RESULTS_URL, params={'page': page_num})
            rows = self.parse_data(html)
            # print(page_num, rows)
            procurements = []
            for row in rows:
                procurements.append(PublicProcurement().from_dict(row, commit=False))
                time.sleep(settings.REQUESTS_DELAY + 1)
            PublicProcurement.objects.bulk_create(procurements)
        self.session.close()
