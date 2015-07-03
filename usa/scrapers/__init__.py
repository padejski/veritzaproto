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
from cpsc import CpscRecallsScraper, CpscRecallsViolationsScraper
from irs_exempt import IrsExemptScraper
from osha  import OshaEbsaScraper, OshaInspectionScraper
from sec_edgar import SecEdgarScraper
from toxics_inventory import ToxicsInventoryScraper

# ============================================================================
# scrapers list
# ============================================================================
usa_scrapers = [FedContractsScraper, FinDisclosuresScraper, SecEdgarScraper,
                CommitteeContributionsScraper, ElectionCandsScraper,
                IndividualContributionsScraper, CpscRecallsScraper,
                CpscRecallsViolationsScraper, IrsExemptScraper,
                OshaEbsaScraper, OshaInspectionScraper, SecEdgarScraper,
                ToxicsInventoryScraper]

# ============================================================================
# EOF
# ============================================================================
