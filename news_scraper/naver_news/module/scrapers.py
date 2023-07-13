import hashlib

from selenium.webdriver.common.by import By


def get_urls_from_next_page(driver, xpaths_dict, page_idx):
    next_page_button_xpath = xpaths_dict["page_2_button_xpath"].replace("a[1]", f"a[{page_idx + 1}]")
    next_page_button = driver.find_element(by=By.XPATH, value=next_page_button_xpath)
    next_page_button.click()
    next_page_article_urls = driver.find_elements(by=By.XPATH, value=xpaths_dict["article_urls_xpath"])
    next_page_article_urls = [article_title.get_attribute("href") for article_title in next_page_article_urls]

    return next_page_article_urls


def get_urls(driver, section_url, xpaths_dict, logger):
    try:
        driver.get(section_url)
    except Exception as e:
        logger.warn(e)
        return "section url unreachable"

    article_urls = driver.find_elements(by=By.XPATH, value=xpaths_dict["article_urls_xpath"])
    article_urls = [article_title.get_attribute("href") for article_title in article_urls]

    for page_idx in range(4):
        try:
            page_2_article_urls = get_urls_from_next_page(driver, xpaths_dict, page_idx)
            article_urls.extend(page_2_article_urls)
        except Exception as e:
            continue

    article_urls = list(set(article_urls))
    return article_urls


def scrape_contents(model, driver, section_key, article_url, xpaths_dict, logger):
    url_md5 = hashlib.md5(article_url.encode("utf-8")).hexdigest()

    if model.objects.filter(url_md5=url_md5).exists():
        return "exists"

    try:
        driver.get(article_url)
    except Exception as e:
        logger.warn(e)
        return "article url unreachable"

    for title_xpath in xpaths_dict["title_xpaths"]:
        try:
            title = driver.find_element(by=By.XPATH, value=title_xpath).text
        except Exception as e:
            title = None
        if title != None:
            break
    title = "" if title == None else title

    for content_xpath in xpaths_dict["content_xpaths"]:
        try:
            content = driver.find_element(by=By.XPATH, value=content_xpath).text
        except Exception as e:
            content = None
        if content != None:
            break
    content = "" if content == None else content

    for image_url_xpath in xpaths_dict["image_url_xpaths"]:
        try:
            image_url = driver.find_element(by=By.XPATH, value=image_url_xpath).get_attribute("src")
        except Exception as e:
            image_url = None
        if image_url != None:
            break
    image_url = "no image" if image_url == None else image_url

    for media_xpath in xpaths_dict["media_xpaths"]:
        try:
            media = driver.find_element(by=By.XPATH, value=media_xpath).get_attribute("alt")
        except Exception as e:
            media = None
        if media != None:
            break
    media = "" if media == None else media

    for published_xpath in xpaths_dict["published_xpaths"]:
        try:
            published = driver.find_elements(by=By.XPATH, value=published_xpath)
            published = published[0].text
        except Exception as e:
            published = None
        if published != None:
            break
    published = "" if published == None else published

    article_data = {
        "url": article_url,
        "url_md5": url_md5,
        "title": title,
        "content": content,
        "section": section_key,
        "image_url": image_url,
        "portal": "naver",
        "media": media,
        "published": published,
    }

    return article_data
