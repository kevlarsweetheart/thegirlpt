import scrapy
import uuid
import re

from thegirl_crawler.items import ThegirlCrawlerItem

from const import *


class ThegirlTestsCrawler(scrapy.Spider):
    name = "thegirl"
    start_urls = START_URLS
    allowed_domains = ALLOWED_DOMAINS

    def parse_test_aggregator_page(self, response):
        test_pages = response.xpath(TEST_LINK_PATH).extract()
        for page in test_pages:
            yield scrapy.Request(URL_PREFIX + page, callback=self.parse_test_page)

    @staticmethod
    def parse_test_page(response):
        _id = str(uuid.uuid4().hex)
        url = response.url
        title = response.xpath(TEST_TITLE_PATH).extract_first()
        tags = []
        for tag in response.xpath(TEST_TAGS_PATH):
            tag_text = tag.xpath(TAG_ITEM_PATH).extract_first()
            tag_text = re.sub(r"[^a-zA-Zа-яА-ЯёЁ0-9\-]", "", tag_text)
            tags.append(tag_text)
        tags = "#".join(tags)

        test = ThegirlCrawlerItem(_id=_id, url=url, title=title, tags=tags)
        yield test

    def parse(self, response, page_num=PAGE_NUM):
        for page in range(1, page_num + 1):
            prefix = response.url.split("-")[0]
            if not prefix.endswith("page"):
                prefix += "page"
            new_page_url = f"{prefix}-{page}/"
            yield scrapy.Request(new_page_url, callback=self.parse_test_aggregator_page)
