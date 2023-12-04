# URLs
START_URLS = ["https://thegirl.ru/tests/page-1/"]
ALLOWED_DOMAINS = ["thegirl.ru"]
URL_PREFIX = "https://www.thegirl.ru"

# XPaths
TEST_LINK_PATH = "//div[contains(@class, 'announcements-page rubric-page__announcements')]//div[@class = " \
                  "'announcements-page__announcement']//span[contains(@class, 'announce-inline__title')]/a/@href"
TEST_TITLE_PATH = "//header[@class = 'article__header']/div[@class = 'article__header-top']/h1[@class = " \
                  "'article__title']//text()"
TEST_TAGS_PATH = "//div[@class = 'tags article-footer__tags']/ul[@class = 'tags__list']/li"
TAG_ITEM_PATH = "./a[@class = 'tags__tag-link']//text()"

# Pagination
PAGE_NUM = 608
