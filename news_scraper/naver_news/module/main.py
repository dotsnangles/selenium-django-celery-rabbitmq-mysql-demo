import os

from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from news_scraper.models import NewsArticle
from news_scraper.naver_news.module.mappers import driver_version, driver_path
from news_scraper.naver_news.module.scrapers import get_urls, scrape_contents
from news_scraper.naver_news.module.logging_utils import get_info_list
from news_scraper.naver_news.module.scraping_utils import get_yesterday


def get_driver():
    options = Options()
    options.add_argument("--headless")

    if not os.path.exists(driver_path):
        GeckoDriverManager(path="selenium_drivers", version=driver_version).install()

    driver = webdriver.Firefox(
        service=FirefoxService(executable_path=driver_path),
        options=options,
    )

    driver.implicitly_wait(5)

    return driver


def main_process(driver, logger, section_key, section_url, xpaths_dict):
    article_urls = get_urls(driver, section_url, xpaths_dict, logger, 4)
    if article_urls == "failed to scrape article urls from section url":
        return False

    yesterday, yesterday_needed = get_yesterday()
    if yesterday_needed:
        yesterday_section_url = section_url + f"&date={yesterday}"
        yesterday_article_urls = get_urls(driver, yesterday_section_url, xpaths_dict, logger, 4)
        if yesterday_article_urls != "failed to scrape article urls from section url":
            article_urls.extend(yesterday_article_urls)

    articles_data = []

    exists_count = 0
    unreachable_article_url_count = 0
    for article_url in article_urls:
        article_data = scrape_contents(NewsArticle, driver, section_key, article_url, xpaths_dict, logger)
        if article_data == "exists":
            exists_count += 1
            continue
        elif article_data == "article url unreachable":
            unreachable_article_url_count += 1
            continue
        articles_data.append(article_data)

    driver.quit()

    obj_creation_count = 0
    orm_exception_count = 0
    for article_data in articles_data:
        try:
            _, created = NewsArticle.objects.get_or_create(url_md5=article_data["url_md5"], defaults=article_data)
            if created:
                obj_creation_count += 1
        except Exception as e:
            logger.warn(e)
            orm_exception_count += 1

    info_list = get_info_list(
        section_key,
        article_urls,
        exists_count,
        articles_data,
        unreachable_article_url_count,
        orm_exception_count,
        obj_creation_count,
    )

    logger.info("\n" + "\n".join(info_list))

    return True
