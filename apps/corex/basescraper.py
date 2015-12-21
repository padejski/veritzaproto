# -*- coding: utf-8 -*-
"""
Module    : basescraper
Date      : May, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : Veritza base scraper abstract class


"""
# ============================================================================
# necessary imports
# ============================================================================
import gzip
import urllib
import zipfile
import StringIO
from datetime import datetime as dt
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup as bs
from django.db import IntegrityError, transaction

import utils


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

    @staticmethod
    def download_ftp(url, gzp=False, zfile=False):
        """download file from ftp server"""
        fhandle = urllib.urlopen(url)

        if gzp:
            fileobj = StringIO.StringIO(fhandle.read())
            fileobj = gzip.GzipFile(fileobj=fileobj)
        elif zfile:
            fileobj = zipfile.ZipFile(StringIO.StringIO(fhandle.read()))
        else:
            fileobj = fhandle

        return fileobj

    def download_http(self, url, zfile=False):
        """download file from an http server"""
        fcontent = self.session.get(url).content

        if zfile:
            fcontent = zipfile.ZipFile(StringIO.StringIO(fcontent))

        return fcontent

    def get(self, url):
        """fetch url """
        res = self.session.get(url, timeout=60)

        return res

    def get_hash(self, obj):
        """get md5 digest of obj"""
        return self.utils.get_hash(obj)

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

    @abstractmethod
    def run(self):
        """run scraper"""
        pass

    @staticmethod
    def save_model(model, report_error=False):
        """save model to database"""
        try:
            with transaction.atomic():
                model.save()
        except IntegrityError as err:
            if report_error:
                raise err

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
    def strip_str(strx, char='\r\n'):
        """strip string and replace characters occurrences
        and remove duplicated spaces.

        """
        strx = ' '.join(strx.strip().replace(char, ' ').split())

        return strx

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
