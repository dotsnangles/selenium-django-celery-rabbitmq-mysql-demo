import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager.settings")

app = Celery(
    "manager",
    include=[
        "news_scraper.naver_news.section_200100",
        "news_scraper.naver_news.section_200101",
        "news_scraper.naver_news.section_200102",
        "news_scraper.naver_news.section_200103",
        "news_scraper.naver_news.section_200104",
        "news_scraper.naver_news.section_200105",
        "news_scraper.naver_news.section_200106",
        "news_scraper.naver_news.section_200107",
    ],
    broker_connection_retry=False,
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=10,
)

app.conf.timezone = "Asia/Seoul"
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "네이버 뉴스 섹션 200100": {"task": "news_scraper.naver_news.section_200100.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200101": {"task": "news_scraper.naver_news.section_200101.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200102": {"task": "news_scraper.naver_news.section_200102.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200103": {"task": "news_scraper.naver_news.section_200103.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200104": {"task": "news_scraper.naver_news.section_200104.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200105": {"task": "news_scraper.naver_news.section_200105.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200106": {"task": "news_scraper.naver_news.section_200106.scrape", "schedule": crontab(minute="*/3")},
    "네이버 뉴스 섹션 200107": {"task": "news_scraper.naver_news.section_200107.scrape", "schedule": crontab(minute="*/3")},
}
