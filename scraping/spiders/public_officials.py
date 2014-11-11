# -*- coding: utf-8 -*-

import urlparse
import scrapy
from scrapy import http
from scrapy import log

from scraping.items import PublicOfficialItem, PublicOfficialReportItem


class PublicOfficialsSpider(scrapy.Spider):
    name = "public-officials"
    allowed_domains = ["www.konfliktinteresa.me"]
    start_urls = [
        "http://www.konfliktinteresa.me/funkcioneri/EvidencijaFun.php",
    ]

    BASE_URL = "http://www.konfliktinteresa.me"
    START_URL = urlparse.urljoin(BASE_URL, "/funkcioneri/EvidencijaFun.php")

    key_map = {
        'name': u'Ime i prezime funkcionera',
        'official_type': u'Vrsta funkcionera',
        'address': u'Adresa',
        'public_office': u'Javna funkcija',
        'public_office_other': u'Druga javna funkcija',
        'job': u'Stalni radni odnos',
        'company_board_member': u'Član organa privrednog društva',
        'salary': u'Mjesečna nadoknada',
        'other_activities': u'Obavljanje drugih djelatnosti',
        'other_activities_salary': u'Mjesečna nadoknada',
        'real_estate': u'Nepokretna imovina',
        'movables': u'Pokretna imovina',
        'movables_others': u'Ostala pokretna imovina',
        'companies': u'Vlasništvo u privrednim društvima',
        'company_salary': u'Mjesečna plata',
        'annual_income': u'Godišnji prihod od poljoprivrede i dr. djelatnosti',
        'other_income': u'Ostali prihodi',
        'credits_debts': u'Krediti, dugovi i potraživanja',

        'spouse': u'Ime bračnog/vanbračnog druga',
        'spouse_job': u'Stalni radni odnos',
        'spouse_other_activities': u'Obavljanje drugih djelatnosti',
        'spouse_real_estate': u'Nepokretna imovina',
        'spouse_movables': u'Pokretna imovina',
        'spouse_movables_others': u'Ostala pokretna imovina',
        'spouse_companies': u'Vlasništvo u privrednim društvima',
        'spouse_company_salary': u'Mjesečna plata',
        'spouse_annual_income': u'Prihodi od poljop,slobod i drugih djeltanosti',
        'spouse_other_income': u'Ostali prihodi',
        'spouse_credits_debts': u'Krediti, dugovi i potraživanja',
    }


    def parse_value(self, html, key, absolute=False):
        prepend = "//" if absolute else "tr/"
        key = self.key_map.get(key)
        if key:
            return ''.join(html.xpath(prepend + "td/font[contains(text(), '" + key + "')]/parent::td/following-sibling::td/font/text()").extract()).strip()
        return ""

    def parse(self, response):
        page_count = int(response.xpath('//table/tr/td/a[1]/@href')[1].re(r'pageNum_Recordset1=(\d+)')[0])
        # for page_num in xrange(0, 1):
        for page_num in xrange(0, page_count):
            yield http.Request(url="{0}?pageNum_Recordset1={1}".format(self.START_URL, page_num), callback=self.parse_officials_links)

    def parse_officials_links(self, response):
        links = filter(self.is_detail_page_link, response.xpath('//table[1]/descendant::table[6]/descendant::a/@href').extract())
        for url in map(self.get_absolute_url, links):
            yield http.Request(url=url, meta={'official_id': self.data_from_url(url, 'ID')}, callback=self.parse_data)

    def parse_data(self, response):
        official_id = response.meta['official_id']

        common_data = {
            'system_id': official_id,
            'name': self.parse_value(response, 'name', absolute=True),
            'official_type': self.parse_value(response, 'official_type', absolute=True),
        }

        official = PublicOfficialItem()
        official['system_id'] = common_data['system_id']
        official['name'] = common_data['name']

        yield official

        for link in response.xpath('//table[1]/descendant::table[5]/descendant::a'):
            url = urlparse.urljoin(self.START_URL, ''.join(link.xpath('@href').extract()).strip())
            disclosure = PublicOfficialReportItem()
            disclosure.update({
                'year': self.data_from_url(url, 'Godina'),
                'rbr': self.data_from_url(url, 'Rbr'),
                'report_name': ''.join(link.xpath('text()').extract()).strip(),
                'link': url,
            })
            disclosure.update(common_data)

            yield http.Request(url=url, meta={'disclosure': disclosure}, callback=self.parse_details)

    def parse_details(self, response):
        disclosure = response.meta['disclosure']
        disclosure.update(self.parse_official(response.xpath('body/div[2]//table[1]/tr/td[2]//table[3]')))
        disclosure.update(self.parse_spouse(response.xpath('body/div[2]//table[1]/tr/td[2]//table[4]')))

        yield disclosure

    # Helper methods
    def parse_spouse(self, table):
        data = {}
        if table:
            table = table[0]
            data = {
                'spouse': self.parse_value(table, 'spouse'),
                'spouse_job': self.parse_value(table, 'spouse_job'),
                'spouse_other_activities': self.parse_value(table, 'spouse_other_activities'),
                'spouse_real_estate': self.parse_value(table, 'spouse_real_estate'),
                'spouse_movables': self.parse_value(table, 'spouse_movables'),
                'spouse_movables_others': self.parse_value(table, 'spouse_movables_others'),
                'spouse_companies': self.parse_value(table, 'spouse_companies'),
                'spouse_company_salary': self.parse_value(table, 'spouse_company_salary'),
                'spouse_annual_income': self.parse_value(table, 'spouse_annual_income'),
                'spouse_other_income': self.parse_value(table, 'spouse_other_income'),
                'spouse_credits_debts': self.parse_value(table, 'spouse_credits_debts'),

                # 'spouse': ''.join(table.xpath('tr[1]/td[2]/font/text()').extract()).strip(),
                # 'spouse_job': ''.join(table.xpath('tr[2]/td[2]/font/text()').extract()).strip(),
                # 'spouse_real_estate': ''.join(table.xpath('tr[4]/td[2]/font/text()').extract()).strip(),
                # 'spouse_movables': ''.join(table.xpath('tr[5]/td[2]/font/text()').extract()).strip(),
                # 'spouse_companies': ''.join(table.xpath('tr[7]/td[2]/font/text()').extract()).strip(),
                # 'spouse_salary': ''.join(table.xpath('tr[8]/td[2]/font/text()').extract()).strip(),
            }
        return data

    def parse_official(self, table):
        data = {}
        if table:
            table = table[0]
            data = {
                'address': self.parse_value(table, 'address'),
                'public_office': self.parse_value(table, 'public_office'),
                'public_office_other': self.parse_value(table, 'public_office_other'),
                'job': self.parse_value(table, 'job'),
                'company_board_member': self.parse_value(table, 'company_board_member'),
                'salary': self.parse_value(table, 'salary'),
                'other_activities': self.parse_value(table, 'other_activities'),
                'other_activities_salary': self.parse_value(table, 'other_activities_salary'),
                'real_estate': self.parse_value(table, 'real_estate'),
                'movables': self.parse_value(table, 'movables'),
                'movables_others': self.parse_value(table, 'movables_others'),
                'companies': self.parse_value(table, 'companies'),
                'company_salary': self.parse_value(table, 'company_salary'),
                'annual_income': self.parse_value(table, 'annual_income'),
                'other_income': self.parse_value(table, 'other_income'),
                'credits_debts': self.parse_value(table, 'credits_debts'),

                # 'address': ''.join(table.xpath('tr[2]/td[2]/font/text()').extract()).strip(),
                # 'public_office': ''.join(table.xpath('tr[3]/td[2]/font/text()').extract()).strip(),
                # 'public_office_other': ''.join(table.xpath('tr[4]/td[2]/font/text()').extract()).strip(),
                # 'job': ''.join(table.xpath('tr[5]/td[2]/font/text()').extract()).strip(),
                # 'companies': ''.join(table.xpath('tr[6]/td[2]/font/text()').extract()).strip(),
                # 'real_estate': ''.join(table.xpath('tr[10]/td[2]/font/text()').extract()).strip(),
                # 'movables': ''.join(table.xpath('tr[11]/td[2]/font/text()').extract()).strip(),
                # 'salary': ''.join(table.xpath('tr[14]/td[2]/font/text()').extract()).strip(),
            }
        return data

    def is_detail_page_link(self, link):
        if link.startswith('EvidFunPrijave.php?ID=') or link.startswith('/funkcioneri/EvidFunPrijave.php?ID='):
            return True
        return False

    def get_absolute_url(self, path):
        return urlparse.urljoin(self.BASE_URL, '/funkcioneri/' + path)

    def data_from_url(self, url, key=None):
        data = dict(urlparse.parse_qsl(urlparse.urlparse(url).query))
        if key:
            return data.get(key)
        return data
