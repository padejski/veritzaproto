"""
serbia scrapers package

"""
from companies import SerbiaCompanyScraper
from officials import SerbiaOfficialsScraper
from procurement import SerbiaProcurementScraper
from elections import SerbiaElectionsScraper


serbia_scrapers = [SerbiaCompanyScraper, SerbiaOfficialsScraper,
                   SerbiaProcurementScraper, SerbiaElectionsScraper]
