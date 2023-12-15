# Import the scrapy module to use its functionalities
import scrapy


# Define a custom Scrapy Item class named 'NewsCrawlItem'
class NewsCrawlItem(scrapy.Item):
    # Each field in the item represents a piece of data that we want to scrape

    # Field to store the headline of a news article
    headline = scrapy.Field()

    # Field to store the summary of the news article
    summary = scrapy.Field()

    # Field to store the URL of the news article
    url = scrapy.Field()

    pass
