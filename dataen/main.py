# Import necessary libraries
import logging
from multiprocessing import Process

import pymongo
from fastapi import FastAPI, HTTPException, Query
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Initialize FastAPI app
app = FastAPI()

# MongoDB's connection details
mongo_conn_str = "mongodb+srv://ahmad:qwerasdf@pythoncluster.mhzcs.mongodb.net/test?authSource=admin&replicaSet=atlas-14oj08-shard-0&readPreference=primary&ssl=true"
client = pymongo.MongoClient(mongo_conn_str)
db = client["news"]
collection = db["crawled_news"]


@app.get("/")
def index():
    # Root endpoint - returns a welcome message
    return "Welcome :) to my news data scraping/crawling application!"


def run_spider(url):
    # Function to run the news spider
    from news_spider import NewsSpider
    process = CrawlerProcess(get_project_settings())
    process.crawl(NewsSpider, start_urls=[url])
    process.start()


def run_spider_in_process(url):
    # Function to run the spider in a separate process
    spider_process = Process(target=run_spider, args=(url,))
    spider_process.start()
    spider_process.join()  # Wait for the process to complete


@app.post("/crawl/")
def crawl_url(url: str):
    # Endpoint to trigger the crawling process for a given news URL
    # this project will deal with BBC news articles (https://www.bbc.com/news/)
    # Article(s) headline, summary, and url will be stored in MongoDB database collection
    try:
        run_spider_in_process(url)
        return {"status": "Crawling completed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def run_spider_article(url):
    # Function to run the article spider
    from news_spider import ArticleSpider
    process = CrawlerProcess(get_project_settings())
    process.crawl(ArticleSpider, url=url)
    process.start()


def run_spider_article_in_process(url):
    # Function to run the article spider in a separate process
    spider_process = Process(target=run_spider_article, args=(url,))
    spider_process.start()
    spider_process.join()  # Wait for the process to complete


@app.post("/crawl-article/")
def crawl_article(url: str):
    # Endpoint to trigger specific article crawling for a given URL
    # For example: (https://www.bbc.com/news/world-europe-67729343)
    # Article author, content text, and url will be stored in MongoDB database collection
    try:
        run_spider_article_in_process(url)
        return {"status": "Article crawling completed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search-articles/")
def search_articles(keyword: str = Query(None, min_length=3)):
    # Endpoint to search articles based on a keyword
    # This will go through either for articles main information or details
    try:
        query = {
            "$or": [
                {"headline": {"$regex": keyword, "$options": "i"}},
                {"article_text": {"$regex": keyword, "$options": "i"}},
                {"summary": {"$regex": keyword, "$options": "i"}}
            ]
        }
        articles = list(collection.find(query, {"_id": 0}))
        return articles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    # Main execution: run the FastAPI app
    try:
        import uvicorn

        uvicorn.run(app, host="127.0.0.1", port=80)
    except Exception as e:
        logging.exception("An error occurred, restarting server...")
