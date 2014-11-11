import re
import time
import urlparse
import math
import requests
import lxml.html

from django.conf import settings

from veritza.apps.core.models import Company

BASE_URL = "http://www.crps.me/CRPSPublic/"
SEARCH_URL = urlparse.urljoin(BASE_URL, "rezultatpretrageregistra.action")
DETAIL_PAGE_URL = urlparse.urljoin(BASE_URL, "prikazidrustvo.action")

RESULTS_PER_PAGE = 15

params = {
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


def get_total_records_count(html):
    for item in html.xpath('//div[@class="prozorpodaci"]/text()'):
        node = item.strip()
        if node:
            return int(re.match("\( Zapisi \d+ - \d+ / (\d+) \)", node, re.UNICODE).groups()[0])
    return 1


def get_page(url, params={}):
    response = requests.get(url, params=params)
    return lxml.html.fromstring(response.content)


def normalize_column_name(name):
    return name.lower().replace(' ', '_')


def parse_members(html, company):
    """
    Parses 'Lica u drustvu' tab on the company detail page
    """
    members = []
    member = {}
    elements = html.xpath('//div[@class="tabbertab"][2]/span | //div[@class="tabbertab"][2]/table')
    for element in elements:
        if element.tag == 'span':
            if member:
                # we reached next member, add current one to the collection and start collecting the next one
                member.update({
                    'registarski_broj': company['registarski_broj'],
                    'link': company['link'],
                })
                members.append(member)
                member = {}
                member = {
                    'title': ''.join(element.xpath('b/text()')).strip(),
                }
        elif element.tag == 'table':
            key = ''.join(element.xpath('descendant::td[1]/b/text()')).lower().replace(':', '').strip()
            value = ''.join(element.xpath('descendant::td[2]/text()')).strip()
            member[key] = value

    # add the last member, obviously there won't be <span> element at the and to designate member data end
    member.update({
        'registarski_broj': company['registarski_broj'],
        'link': company['link'],
    })
    members.append(member)

    # if members:
    #     print(members)
    return members


def parse_detail_page(html, company):
    """
    registration date, full name, headquarters address, mail address

    """
    field_values = [field.strip() for field in html.xpath('//div[@class="tabbertab"][1]/b/following-sibling::text()') if field.strip()]
    company_members = parse_members(html, company)
    # print(company_members)
    # scraperwiki.sql.save(['registarski_broj', 'ime', 'title'], data=company_members, table_name='company_members')
    # return {
    #     'full_name': field_values[3],
    #     'address': "%s, %s" % (field_values[6], field_values[7]),
    #     'mail_address': "%s, %s" % (field_values[8], field_values[9]),
    #     'registration_date': field_values[10],
    # }
    return {
        'full_name': ''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Puni naziv")]/following-sibling::text()[1]')).strip(),
        'address': "%s, %s" % (''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Adresa sjedi")]/following-sibling::text()[1]')).strip(),
                                ''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Mjesto sjedi")]/following-sibling::text()[1]')).strip()),
        'mail_address': "%s, %s" % (''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Adresa prijema slu")]/following-sibling::text()[1]')).strip(),
                                ''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Mjesto prijema slu")]/following-sibling::text()[1]')).strip()),
        'registration_date': ''.join(html.xpath('//div[@class="tabbertab"][1]/b[contains(text(), "Datum registracije")]/following-sibling::text()[1]')).strip(),
    }


def collect_rows(html):
    try:
        table = html.xpath('//div[@class="prozorpodaci"]/table')[0]
        columns = map(normalize_column_name, table.xpath('tr[@class ="naslov"]/td/text()'))  # + ['lat', 'lng']
        companies = []
        for row in table.xpath('tr')[1:]:
            fields = []
            for cell in row.xpath('td')[:-2]:  # last two cells contain buttons, not data
                fields.append(cell.xpath('text()')[0].strip())
            company = dict(zip(columns, fields))

            # get more details from the detail pages
            id_dosijea = ''.join(row.xpath('td[8]/form/input[@type="hidden"]/@value'))
            company.update({'link': "%s%s%s" % (DETAIL_PAGE_URL, '?idDosijea=', id_dosijea)})
            company.update(parse_detail_page(get_page(DETAIL_PAGE_URL, {'idDosijea': id_dosijea}), company))
            companies.append(company)
        return companies
    except IndexError as e:
        print(e)
        return []


def run(start_page=0, end_page=None):
    html = get_page(SEARCH_URL, params=params)

    page_count = int(math.floor(get_total_records_count(html) / float(RESULTS_PER_PAGE)))
    page_count = end_page or page_count
    for page_num in xrange(start_page, page_count):
        params.update({'od': page_num * RESULTS_PER_PAGE + 1})
        for company_data in collect_rows(get_page(SEARCH_URL, params=params)):
            #scraperwiki.sql.save(['registarski_broj'], company)
            print(company_data)
            company = Company().from_dict(company_data, commit=False)
            company.save()
            time.sleep(settings.REQUESTS_DELAY)
