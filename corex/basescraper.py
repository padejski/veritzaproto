"""
Module    : basescraper
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza base scraper abstract class


"""
# ============================================================================
# necessary imports
# ============================================================================
from hashlib import md5
from datetime import datetime as dt

import utils
import requests
from bs4 import BeautifulSoup as bs


# ============================================================================
# BaseScraper class
# ============================================================================
class BaseScraper(object):
    """Scraper base class """
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140610 " \
        "Firefox/24.0 Iceweasel/24.6.0"

    def __init__(self):
        """Initialize base scraper"""
        self.utils = utils
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.user_agent})

    def get(self, url):
        """fetch url """
        res = self.session.get(url, timeout=60)

        return res

    @staticmethod
    def get_hash(obj):
        """get md5 digest of obj"""
        return md5(str(obj)).digest().decode("iso-8859-1")

    def get_soup(self, url):
        """beautifulsoup of url contents"""
        soup = bs(self.session.get(url).content)

        return soup

    @staticmethod
    def get_soup_basic(url):
        """beautifulsoup of url"""
        soup = bs(requests.get(url).content)

        return soup

    def post(self, *args, **kwargs):
        """post to url """
        res = self.session.post(*args, **kwargs)

        return res

    def post_soup(self, *args, **kwargs):
        """get post response as beautifulsoup"""
        soup = bs(self.session.post(*args, **kwargs).content)

        return soup

    @staticmethod
    def str2date(datestr, fmt, sep=None):
        """Convert datestr to date

        """
        if not datestr:
            return None

        if sep:
            datestr = datestr.split(sep)[0]

        return dt.strptime(datestr, fmt).date()

    @staticmethod
    def update_model(new, old):
        """update old model's content

        args:
            new (obj): database model
            old (obj): database model

        returns: None

        """
        if new.hash != old.hash:
            old.__dict__.update(new.__dict__)
            old.save()
# ============================================================================
# EOF
# ============================================================================
