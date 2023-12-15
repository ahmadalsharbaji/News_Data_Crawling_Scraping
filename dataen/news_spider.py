# Import necessary modules
import re

import scrapy

from dataen.items import NewsCrawlItem


# Define the NewsSpider class for scraping news headlines, summaries, and urls
class NewsSpider(scrapy.Spider):
    name = 'news'  # Name of the spider
    start_urls = ['https://www.bbc.com/news/']  # Initial URL to start scraping

    def parse(self, response):
        # Extract headline list using CSS selectors
        headline_list = response.css("h3.gs-c-promo-heading__title.gel-pica-bold.nw-o-link-split__text::text").extract()

        # Extract summary list using CSS selectors
        summary_list = response.css("p.gs-c-promo-summary.gel-long-primer.gs-u-mt.nw-c-promo-summary::text").extract()

        # Extract URLs list using XPath
        urls_list = response.xpath(
            "//a[contains(@class, 'gs-c-promo-heading') and contains(@class, 'gs-o-faux-block-link__overlay-link') and contains(@class, 'gel-pica-bold') and contains(@class, 'nw-o-link-split__anchor')]/@href").extract()

        base_url = 'https://www.bbc.com'  # Base URL for constructing full URLs
        for headline, summary, url in zip(headline_list, summary_list, urls_list):
            item = NewsCrawlItem()  # Create a new item
            item['headline'] = headline  # Set the headline
            item['summary'] = summary  # Set the summary
            # Create the full URL
            full_url = url if url.startswith('http') else base_url + url
            item['url'] = full_url  # Set the URL

            yield item  # Yield the filled item for processing


# Define the ArticleSpider class for scraping full articles (author, content text, and url)
class ArticleSpider(scrapy.Spider):
    name = 'article'  # Name of the spider

    def __init__(self, url=None, *args, **kwargs):
        super(ArticleSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]  # Set the URL to scrape

    def parse(self, response):
        author = response.css("div.ssrcss-68pt20-Text-TextContributorName.e8mq1e96::text").get()
        # Extract the author's name, remove 'By ' prefix if present
        if author and author.startswith("By "):
            author = author[3:]

        # Extract the article text
        article_text = " ".join(response.css("p.ssrcss-1q0x1qg-Paragraph.e1jhz7w10::text").extract())

        # Remove a specific disclaimer text from the article text using regular expressions
        disclaimer_pattern = r'© \d{4} BBC\. The BBC is not responsible for the content of external sites\.'
        article_text = re.sub(disclaimer_pattern, '', article_text).strip()

        # Yield the scraped data
        yield {
            'author': author,
            'article_text': article_text,
            'url': response.url  # Include the URL of the article
        }
