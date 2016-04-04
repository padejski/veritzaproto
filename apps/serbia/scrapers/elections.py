# -*- coding: utf-8 -*-
"""
Serbia's Elections Donations scraper

__author__ = Matt Gathu <mattgathu@gmail.com>
__date__ = May 2015

"""
# ============================================================================
# necessary imports
# ============================================================================
import string
import itertools

from apps.corex.basescraper import BaseScraper
from .. import models

# ============================================================================
# useful constants
# ============================================================================
BASE_URL = 'http://www.acas.rs/acasPublic/pretragaPrilogaLica.htm'
DETAILS_URL = 'http://www.acas.rs/acasPublic/pretragaPrilogaLicaDetails.htm'
COOKIES = {'pll_language': 'en',
           'stl_default_lang': 'cir',
           'em_transient_id': 'emtr_165d7f9a629e4563110b06dcbe91b5b744d1d120'}

HEADERS = {'Accept': 'application/json, text/javascript, */*',
           'Content-Length': 118,
           'Content-Type': 'application/x-www-form-urlencoded',
           'Host': 'www.acas.rs',
           'Origin': 'http://www.acas.rs',
           'Referer': BASE_URL,
           'X-Requested-With': 'XMLHttpRequest'}

PAYLOAD = {'sEcho': 2, 'sColumns': '',
           'iDisplayStart': 0,
           'mDataProp_0': 0, 'mDataProp_1': 1,
           'mDataProp_2': 2, 'mDataProp_3': 3,
           'prilogPolitickogSubjekta.liceIme': '',
           'politickiSubjekt.id': '',
           'politickiSubjektNaziv': '',
           'izbor.id': '',
           'izborNaziv_': ''}

NAMES = ['Јовановић', 'Никола', 'Лука', 'Лазар', 'Вук', 'Стефан', 'Алекса',
         'Марко']


# ============================================================================
# scraper implementation
# ============================================================================
class SerbiaElectionsScraper(BaseScraper):
    """Serbian Elections Donations Scraper"""
    NAME = 'serbia:elections'

    def __init__(self):
        """initialize base class"""
        BaseScraper.__init__(self)

    def gen_donations(self):
        """generate election donations

        args: None

        yields: donation (dict): dictionary of donation info

        """
        names = (name for name in self.gen_names())
        donors = self.parse_donors(self.get_donors(names))

        for donation in self.get_donors_donations(donors):
            yield donation

    def gen_names(self):
        """generate search names

        self.gen_names() -> search_names_iterable

        args: None

        yields: name (str) : search name

        """
        cnames = (c.name for c in models.Company.objects.all())
        onames = (o.name for o in models.Official.objects.all())

        for names in itertools.chain(NAMES, cnames, onames):
            for name in names.strip().split(' '):
                name = self.remove_punctuation(name)
                if len(name) > 4:
                    print(name)
                    yield name

    def get_donors_donations(self, donors):
        """fetch donor's donation

        args: donations (iterable): list of donors dicts

        yields: donation (dict) donation data dictionary

        """
        for donor in donors:
            for donation in self.get_donor_donations(donor):
                yield donation

    def get_donor_donations(self, donor):
        """fetch donor details

        args:
            donor (dict): donor dictionary with id key

        yields:
            donation (dict): donatio data dict

        """
        payload = {'iColumns': 6,
                   'iDisplayLength': 10,
                   'mDataProp_4': 4,
                   'mDataProp_5': 5,
                   'prilogPolitickogSubjekta.liceId': donor['id'],
                   'prilogPolitickogSubjekta.licePrezime': donor['search_name']}

        payload.update(PAYLOAD)

        self.session.close()
        self.session.headers.update(HEADERS)

        det = self.post(DETAILS_URL, data=payload, cookies=COOKIES).json()
        hds = ['donation', 'kind_donations', 'dues', 'amount',
               'selection', 'political_party']

        for donation in det['aaData']:
            donation = dict(zip(hds, donation))
            donation['donor_name'] = donor['name']
            donation['url'] = BASE_URL

            yield donation

    def _get_donors(self, search_name):
        """fetch donors data from ajax endpoint"""
        payload = {'iColumns': 4,
                   'iDisplayLength': 100,
                   'prilogPolitickogSubjekta.liceId': '',
                   'prilogPolitickogSubjekta.licePrezime': search_name}

        payload.update(PAYLOAD)

        self.session.headers.update(HEADERS)

        donors_num = self.get_donors_num(payload)

        for interval in range(0, donors_num, 100):
            payload['iDisplayStart'] = interval

            res = self.post(BASE_URL, data=payload, cookies=COOKIES)

            donor = res.json()
            donor['search_name'] = search_name

            yield donor

    def get_donors(self, search_names):
        """get election donors """
        for name in search_names:
            for donor in self._get_donors(name):
                yield donor

    def get_donors_num(self, payload):
        """get maximum number of donors from data endpoint"""
        self.session.headers.update(HEADERS)
        res = self.post(BASE_URL, data=payload, cookies=COOKIES)

        self.session.close()

        try:
            return int(res.json()['iTotalRecords'])
        except ValueError:
            print(res.text)
            return 0

    @staticmethod
    def parse_donors(donor_data):
        """parse donors json data"""
        for data in donor_data:
            search_name = data['search_name']
            data = data['aaData']
            hds = ['id', 'name']
            for item in data:
                donor_dict = dict(zip(hds, item[1:-1]))
                donor_dict['search_name'] = search_name

                yield donor_dict

    @staticmethod
    def remove_punctuation(strx):
        """remove punctuation from string """
        exclude = set(string.punctuation)

        return ''.join(ch for ch in strx if ch not in exclude)

    def run(self):
        """run scraper"""
        for donation in self.gen_donations():
            donation['hash'] = self.get_hash(donation)
            model = models.ElectionDonation(**donation)
            self.save_model(model)
            yield


if __name__ == '__main__':
    pass
# ============================================================================
# EOF
# ============================================================================
