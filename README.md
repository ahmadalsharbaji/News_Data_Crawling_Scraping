# News Data Scraping Project
# Overview
This project is designed to scrape and collect news data specifically from the BBC News website. It uses Python with Scrapy for web scraping, FastAPI for serving API endpoints, and MongoDB for data storage.

Hosted version on Azure Cloud. For a step-by-step guide, please refer to the screenshots provided in the repository.

# Features
- Scraping headlines, summaries, and URLs from news homepages.
- Scraping full articles including text and author information.
- API endpoints for triggering scrapes and searching articles.
- Data storage in MongoDB for easy retrieval and management.
# Installation
Prerequisites:
- Python 3.9
- MongoDB
# Setup
- Clone the repository:
  
`git clone https://github.com/ahmadalsharbaji/News_Data_Crawling_Scraping.git`
- Install required Python packages:

`pip install -r requirements.txt`

# Usage
Running the Server

Start the FastAPI server:
`python main.py`
# API Endpoints
`GET /` - Welcome message.

`POST /crawl/` - Trigger news homepage scraping.

`POST /crawl-article/` - Trigger specific article scraping.

`GET /search-articles/` - Search articles with a keyword.

# You can run this project locally following the setup instructions, or visit the hosted version on Azure Cloud. For a step-by-step guide, please refer to the screenshots provided in the repository.

Access the application:

Locally: Run it on your machine following the setup guide.

Hosted version:
- Main application: http://172.171.82.16/
- FastAPI Swagger Documentation: http://172.171.82.16/docs


# Using Endpoints via Bash Terminal
You can interact with the API using `curl` commands in the terminal:

- Crawl and scrape news articles:

`curl -X POST "http://127.0.0.1:80/crawl/?url=https://www.bbc.com/news"`
- Crawl and scrape a specific article:

`curl -X POST "http://127.0.0.1:80/crawl-article/?url=https://www.bbc.com/news/world-asia-china-67689072"`
- Search for articles by keyword:

`curl "http://127.0.0.1:80/search-articles/?keyword=repercussions"`

# Scraping
The project uses Scrapy spiders for scraping:

- `NewsSpider` for scraping news headlines and summaries.
- `ArticleSpider` for scraping full articles.

# Data Storage
Scraped data is stored in MongoDB:

- Database: `news`
- Collection: `crawled_news`

# Contributing
Contributions to improve the project are welcome. Please follow these steps:

1- Fork the repository.

2- Create a new branch for your feature.

3- Commit your changes.

4- Push to the branch.

5- Submit a pull request.

Your interest and contributions are highly valued. Happy scraping!
