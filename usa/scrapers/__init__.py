"""
US Federal Level Scrapers

"""
from sec_edgar import SecEdgarScraper
from procurement import FedContractsScraper
from financial_disclosure import FinDisclosuresScraper

usa_scrapers = [FedContractsScraper, FinDisclosuresScraper, SecEdgarScraper]
