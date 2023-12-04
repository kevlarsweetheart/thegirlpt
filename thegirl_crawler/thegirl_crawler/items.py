import scrapy


class ThegirlCrawlerItem(scrapy.Item):
    _id = scrapy.Field()  # Randomly generated test ID
    url = scrapy.Field()  # Test initial URL
    title = scrapy.Field()  # Test title
    tags = scrapy.Field()  # Manually defined test tags
