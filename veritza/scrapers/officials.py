#!/usr/bin/env python
import re
import time
import urlparse
import requests
import lxml.html

from django.conf import settings

from veritza.apps.core.models import PublicOfficialReport

STRING_NOT_FOUND = -1
BASE_URL = "http://www.konfliktinteresa.me"
START_URL = urlparse.urljoin(BASE_URL, "/funkcioneri/EvidencijaFun.php")

DISCLOSURE_TYPES = {
    '1': 'Annual disclosure',
    '2': 'Start on End disclosure',
    '3': 'Change disclosure',
}


class OfficialsScraper(object):

    def get(self, url, params={}):
        return lxml.html.fromstring(requests.get(url, params=params).content)

    def post(self, url, data={}):
        return lxml.html.fromstring(requests.get(url, data=data).content)

    def get_page_count(self, html):
        return int(self.re(r'pageNum_Recordset1=(\d+)', html.xpath('//table/tr/td/a[1]/@href')[1]))

    def is_detail_page_link(self, link):
        if link.startswith('EvidFunPrijave.php?ID=') or link.startswith('/funkcioneri/EvidFunPrijave.php?ID='):
            return True
        return False

    def get_absolute_url(self, path):
        return urlparse.urljoin(BASE_URL, '/funkcioneri/' + path)

    def data_from_url(self, url, key=None):
        data = dict(urlparse.parse_qsl(urlparse.urlparse(url).query))
        if key:
            return data.get(key)
        return data

    def id_from_url(self, url):
        return self.data_from_url(url, 'ID')

    def year_from_url(self, url):
        return self.data_from_url(url, 'Godina')

    def type_from_url(self, url):
        return self.data_from_url(url, 'Rbr')

    def re(self, pattern, text):
        match = re.search(pattern, text)
        if match and match.groups():
            return match.groups()[0]
        return ""

    def get_officials_links(self, html):
        links = filter(self.is_detail_page_link, html.xpath('//table[2]/descendant::table[6]/descendant::a/@href'))
        return map(self.get_absolute_url, links)

    def parse_children(self, table=None):
        return {}

    def parse_spouse(self, table):
        data = {}
        if table:
            table = table[0]
            data = {
                'spouse': ''.join(table.xpath('tr[1]/td[2]/font/text()')).strip(),
                'spouse_job': ''.join(table.xpath('tr[2]/td[2]/font/text()')).strip(),
                'spouse_real_estate': ''.join(table.xpath('tr[4]/td[2]/font/text()')).strip(),
                'spouse_movables': ''.join(table.xpath('tr[5]/td[2]/font/text()')).strip(),
                'spouse_companies': ''.join(table.xpath('tr[7]/td[2]/font/text()')).strip(),
                'spouse_salary': ''.join(table.xpath('tr[8]/td[2]/font/text()')).strip(),
            }
        return data

    def parse_official(self, table):
        data = {}
        if table:
            table = table[0]
            data = {
                'address': ''.join(table.xpath('tr[2]/td[2]/font/text()')).strip(),
                'public_office': ''.join(table.xpath('tr[3]/td[2]/font/text()')).strip(),
                'public_office_other': ''.join(table.xpath('tr[4]/td[2]/font/text()')).strip(),
                'job': ''.join(table.xpath('tr[5]/td[2]/font/text()')).strip(),
                'companies': ''.join(table.xpath('tr[6]/td[2]/font/text()')).strip(),
                'real_estate': ''.join(table.xpath('tr[10]/td[2]/font/text()')).strip(),
                'movables': ''.join(table.xpath('tr[11]/td[2]/font/text()')).strip(),
                'salary': ''.join(table.xpath('tr[14]/td[2]/font/text()')).strip(),
            }
        return data

    def parse_disclosure(self, html):
        data = {}
        data.update(self.parse_official(html.xpath('body/div[2]//table[1]/tr/td[2]//table[3]')))
        data.update(self.parse_spouse(html.xpath('body/div[2]//table[1]/tr/td[2]//table[4]')))
        data.update(self.parse_children())
        return data

    def parse_data(self, html, official_id):
        disclosures = []

        common_data = {
            'id': official_id,
            'name': ''.join(html.xpath('body/div[2]//table[1]/tr/td[2]//table[1]/tr[1]/td[2]/font/text()')).strip(),
            'official_type': ''.join(html.xpath('body/div[2]//table[1]/tr/td[2]//table[1]/tr[2]/td[2]/font/text()')).strip(),
        }

        for link in html.xpath('//table[2]/descendant::table[5]/descendant::a'):
            url = urlparse.urljoin(START_URL, ''.join(link.xpath('@href')).strip())
            disclosure = {
                'year': self.year_from_url(url),
                'rbr': self.type_from_url(url),
                'report_name': ''.join(link.xpath('text()')).strip(),
                'link': url,
            }
            disclosure.update(common_data)
            disclosure.update(self.parse_disclosure(self.get(url)))
            # print(url, disclosure)
            disclosures.append(disclosure)
        return disclosures

    def run(self, start_page=0, end_page=None):
        html = self.get(START_URL)
        page_count = self.get_page_count(html)
        page_count = end_page or page_count
        #for page_num in xrange(0, page_count+1): # there are 112 pages
        for page_num in xrange(start_page, page_count):
            html = self.get(START_URL, params={'pageNum_Recordset1': page_num})
            # print(len(self.get_officials_links(html)))
            for url in self.get_officials_links(html):
                official_id = self.id_from_url(url)
                disclosures = self.parse_data(self.get(url), official_id)
                reports = []
                for disclosure in disclosures:
                    reports.append(PublicOfficialReport().from_data(disclosure, commit=False))
                PublicOfficialReport.objects.bulk_create(reports)
                time.sleep(settings.REQUESTS_DELAY)
