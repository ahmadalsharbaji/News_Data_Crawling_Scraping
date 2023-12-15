# Scrapy's settings for dataen project

BOT_NAME = "dataen"

SPIDER_MODULES = ["dataen"]
NEWSPIDER_MODULE = "dataen"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    "dataen.pipelines.NewsCrawlPipeline": 300,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
