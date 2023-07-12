import os

from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from celery import shared_task
from manager.celery import app

from news_scraper.models import NewsArticle
from news_scraper.naver_news.module.mappers import section_dict, xpaths_dict, driver_version, driver_path
from news_scraper.naver_news.module.scrapers import get_urls, scrape_contents
from news_scraper.naver_news.module.logging_utils import get_info_list

import logging

logger = logging.getLogger(__name__)

section_key = "200101"

section_url = f"https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={section_dict[section_key]}&listType=summary"


@shared_task
def scrape():
    options = Options()
    options.add_argument("--headless")

    if not os.path.exists(driver_path):
        GeckoDriverManager(path="selenium_drivers", version=driver_version).install()

    driver = webdriver.Firefox(
        service=FirefoxService(executable_path=driver_path),
        options=options,
    )

    driver.implicitly_wait(10)

    article_urls = get_urls(driver, section_url, xpaths_dict["article_urls_xpath"])

    articles_data = []

    exist_count = 0
    for article_url in article_urls:
        article_data = scrape_contents(NewsArticle, driver, section_key, article_url, xpaths_dict)
        if article_data == None:
            exist_count += 1
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

    info_list = get_info_list(article_urls, exist_count, len(articles_data), orm_exception_count, obj_creation_count)

    logger.info("\n" + "\n".join(info_list))

    return "finished."
