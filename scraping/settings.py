# Scrapy settings for scraping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'veritza_bot'

SPIDER_MODULES = ['scraping.spiders']
NEWSPIDER_MODULE = 'scraping.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraping (+http://www.yourdomain.com)'
USER_AGENT = "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'veritza.settings.dev'


ITEM_PIPELINES = {"scraping.pipelines.VeritzaModelsPipeline": 10}

DOWNLOAD_DELAY = 0.5  # seconds

DUPEFILTER_CLASS = "scraping.DBDupeFilter"