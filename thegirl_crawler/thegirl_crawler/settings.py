BOT_NAME = "thegirl_crawler"

SPIDER_MODULES = ["thegirl_crawler.spiders"]
NEWSPIDER_MODULE = "thegirl_crawler.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 5

# Configure item pipelines
ITEM_PIPELINES = {
   "thegirl_crawler.pipelines.ThegirlCrawlerPipeline": 300,
}
