from celery import shared_task
from manager.celery import app

from news_scraper.naver_news.module.mappers import section_dict, xpaths_dict_107 as xpaths_dict
from news_scraper.naver_news.module.main import get_driver, main_process

import logging

logger = logging.getLogger(__name__)

section_key = "200107"

section_url = f"https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={section_dict[section_key]}&listType=summary"


@shared_task
def scrape():
    driver = get_driver()
    result = main_process(driver, logger, section_key, section_url, xpaths_dict)
    if result:
        return "finished."
    else:
        return "error occured during main process."
