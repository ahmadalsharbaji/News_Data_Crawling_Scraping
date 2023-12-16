# Import the pymongo module to work with MongoDB

from dataen.main import collection


# Define the NewsCrawlPipeline class
class NewsCrawlPipeline:

    def process_item(self, item, spider):
        try:
            collection.insert_one(dict(item))
        except Exception as e:
            spider.logger.error(f"Error inserting item: {e}")
            # Optionally, re-raise the exception if you want to halt the pipeline
        return item
