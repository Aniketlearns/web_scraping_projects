# Scrapy settings for iplt20 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "iplt20"

SPIDER_MODULES = ["iplt20.spiders"]
NEWSPIDER_MODULE = "iplt20.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "iplt20 (+http://www.yourdomain.com)"
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'


# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
# COOKIES_ENABLED = True
# cookies = {
# COOKIES_ENABLED = {
#     'AWSALB': 'rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf',
#     'AWSALBCORS': 'rBkjMx+fkGw8JhtenIKOGzEdTLahf6ATR7LN9nls4kFhCCFP7+PL9G45m3Q+xpqg5JnYYg/QfTnVVTb491b6J3wWLRe5qMCHRcMbypKWpW1h7PjtSmMM5WJJglVf',
#     'laravel_session': 'eyJpdiI6IkFVUW1LRkNjTm9Yd2JCTUhQamZkZ2c9PSIsInZhbHVlIjoiNGJjbWxoV2V4UHRESE5DejVnQUdacC9GaG1MUlRXK0pOblNFS2dhdmZpWGFhRHdRMlV3N0ZhNkdNN2ZpOW1rYmpCQkZDeEd2cjB5bU9DSTFmcmVZSVR1UkJBVFptYlg5aXJJVEM3bHZ0cUlTem5UcUw1WTJPMzRBM2pDajJqWUYiLCJtYWMiOiI1ZWNhZWU0MWE1OGJjNmFkNzYyYmZmOTU2ZDRmNWU5Nzk3NGU4Y2RlMzE0OGNjODgwNDkwMDU0YmVhZTdlZjI1IiwidGFnIjoiIn0%3D',
# }

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
#     'accept-language': 'en-GB,en;q=0.8',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Brave";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'sec-gpc': '1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "iplt20.middlewares.Iplt20SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "iplt20.middlewares.Iplt20DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "iplt20.pipelines.Iplt20Pipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
