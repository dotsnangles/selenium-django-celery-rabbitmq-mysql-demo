def get_info_list(article_urls, exist_count, num_new_articles, orm_exception_count, obj_creation_count):
    info_list = [
        f"### number of article urls: {len(article_urls)}",
        f"### number of article urls found in db before scraping: {exist_count}",
        f"### number of articles scraped: {num_new_articles}",
        f"### number of orm exceptions: {orm_exception_count}",
        f"### number of duplicate rows found updaing db: {num_new_articles - obj_creation_count}",
        f"### number of new rows added to db: {obj_creation_count}",
    ]
    return info_list
