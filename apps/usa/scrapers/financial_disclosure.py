"""
Federal Financial Disclosures Scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = June 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
import itertools
from itertools import imap

from apps.corex.basescraper import BaseScraper
from ..models import FedFinancialDisclosure

# ============================================================================
# useful constants
# ============================================================================
BASE_URL = 'http://clerk.house.gov/public_disc/financial-search.aspx'
PDF_URL = 'http://clerk.house.gov/public_disc/{}'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '3265',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'clerk.house.gov',
    'Origin': 'http://clerk.house.gov',
    'Referer': 'http://clerk.house.gov/public_disc/financial-search.aspx.'
}


# ============================================================================
# scraper implementation
# ============================================================================
class FinDisclosuresScraper(BaseScraper):
    """USA Federal financial disclosures scraper"""
    NAME = 'usa:financial-disclosures'

    def __init__(self):
        """Initialize base scraper"""
        BaseScraper.__init__(self)

    def fetch_data(self, data):
        """post search form data and get response"""
        self.session.close()
        self.session.headers.update(HEADERS)

        soup = self.post_soup(BASE_URL, data=data)

        for data in self.scrape_data(soup):
            yield data

    def gen_data(self):
        """fetch data iteratively from data endpoint"""
        form = self.get_soup(BASE_URL).find('form')
        states = self.get_states(form)
        years = self.get_years(form)
        form = self.get_form_fields(form)

        for form_data in self.gen_form_data(form, states, years):
            for data in self.fetch_data(form_data):
                yield data

    @staticmethod
    def gen_form_data(form, states, years):
        """Generate search form data combinations

        args:
            form (dict): search form skeleton dictionary with fields
                         as keys.
            states (list): list of federal states
            years (list): list of years

        yields:
            form_data (dict)

        """
        for state, year in itertools.product(states, years):
            form['ctl00$cphMain$ddlState'] = state
            form['ctl00$cphMain$txbFiling_year'] = year

            yield form

    @staticmethod
    def get_form_fields(form):
        """Get search form fields"""
        fields = {f.get('name'): f.get('value', '') for f
                  in form.find_all('input')}

        return fields

    @staticmethod
    def get_states(form):
        """Get federal states from selection list"""
        select = form.find('select', {'name': 'ctl00$cphMain$ddlState'})
        states = [opt.get('value') for opt in select.find_all('option')[1:]]

        return states

    @staticmethod
    def get_years(form):
        """Get years from select list"""
        select = form.find('select', {'name': 'ctl00$cphMain$txbFiling_year'})
        years = [opt.get('value') for opt in select.find_all('option')[1:]]

        return years

    def run(self):
        """run scraper"""
        for data in self.gen_data():
            model = FedFinancialDisclosure(**data)
            self.save_model(model)

            yield

    def scrape_data(self, soup):
        """Scrape data from page content soup"""
        rows = soup.find('table', {'id': 'search_results'}).find_all('tr')[1:]

        # remove paging row
        for idx, row in enumerate(rows):
            if row.get('class')[0] == 'pagingRow':
                rows.pop(idx)

        for data in imap(self.scrape_datarow, rows):
            yield data

    def scrape_datarow(self, row):
        """Scrape data row into a python dict"""
        def _scrape_row():
            """scrape data from row"""
            pdf_link = PDF_URL.format(row.find('a').get('href'))
            fields = [x.text.strip() for x in row.find_all('td')]
            fields.append(pdf_link)

            return fields

        data = dict(zip(['name', 'office', 'year', 'filing', 'pdf'],
                        _scrape_row()))
        data['name'] = self.strip_str(data['name'])
        data['hash'] = self.get_hash(data)

        return data


# ============================================================================
# EOF
# ============================================================================
