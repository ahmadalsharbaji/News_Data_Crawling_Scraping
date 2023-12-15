# Import the pymongo module to work with MongoDB
import pymongo


# Define the NewsCrawlPipeline class
class NewsCrawlPipeline:

    def __init__(self):
        # Initialize a connection to MongoDB
        self.conn = pymongo.MongoClient(
            "mongodb+srv://ahmad:qwerasdf@pythoncluster.mhzcs.mongodb.net/test?authSource=admin&replicaSet=atlas-14oj08-shard-0&readPreference=primary&ssl=true"
        )

        # Connect to the 'news' database
        mydb = self.conn["news"]

        # Connect to the 'crawled_news' collection
        self.collection = mydb["crawled_news"]

    def process_item(self, item, spider):
        # Insert the scraped item into the MongoDB collection
        self.collection.insert_one(dict(item))

        # Return the item after processing
        return item
