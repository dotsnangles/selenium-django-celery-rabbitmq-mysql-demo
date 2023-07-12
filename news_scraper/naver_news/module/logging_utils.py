def get_info_list(
    section_key,
    article_urls,
    exists_count,
    articles_data,
    unreachable_article_url_count,
    orm_exception_count,
    obj_creation_count,
):
    info_list = [
        f"### section: {section_key}",
        f"### number of article urls: {len(article_urls)}",
        f"### number of article urls found in db before scraping: {exists_count}",
        f"### number of article urls unreachable: {unreachable_article_url_count}",
        f"### number of articles scraped: {len(articles_data)}",
        f"### number of orm exceptions: {orm_exception_count}",
        f"### number of duplicate rows found updaing db: {len(articles_data) - obj_creation_count}",
        f"### number of new rows added to db: {obj_creation_count}",
    ]
    return info_list
