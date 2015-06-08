"""
US Federal Level Scrapers

"""
# ============================================================================
# import scrapers
# ============================================================================
from sec_edgar import SecEdgarScraper
from procurement import FedContractsScraper
from financial_disclosure import FinDisclosuresScraper
from elections import CommitteeContributionsScraper, ElectionCandsScraper
from elections import IndividualContributionsScraper

# ============================================================================
# scrapers list
# ============================================================================
usa_scrapers = [FedContractsScraper, FinDisclosuresScraper, SecEdgarScraper,
                CommitteeContributionsScraper, ElectionCandsScraper,
                IndividualContributionsScraper]

# ============================================================================
# EOF
# ============================================================================
