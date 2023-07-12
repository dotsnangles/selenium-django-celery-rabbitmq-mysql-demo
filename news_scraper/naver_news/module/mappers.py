driver_version = "v0.33.0"
driver_path = f"selenium_drivers/.wdm/drivers/geckodriver/linux64/{driver_version}/geckodriver"

section_dict = {
    "200100": "100",
    "200101": "101",
    "200102": "102",
    "200103": "103",
    "200104": "104",
    "200105": "105",
    "200106": "106",
    "200107": "107",
}

xpaths_dict = dict(
    article_urls_xpath='//*[@id="main_content"]/div[2]/ul/li/dl/dt/a',
    title_xpaths=[
        '//*[@id="title_area"]/span',
        '//*[@id="content"]/div[1]/div/h2',
        '//*[@id="content"]/div/div[1]/div/div[1]/h4',
    ],
    media_xpaths=[
        '//*[@id="ct"]/div[1]/div[1]/a/img[1]',
        '//*[@id="content"]/div[1]/div/div[1]/a/img',
        '//*[@id="pressLogo"]/a/img',
    ],
    content_xpaths=[
        '//*[@id="dic_area"]',
        '//*[@id="articeBody"]',
        '//*[@id="newsEndContents"]',
    ],
    published_xpaths=[
        '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span',
        '//*[@id="content"]/div[1]/div/div[2]/span/em',
        '//*[@id="content"]/div/div[1]/div/div[1]/div/span[1]',
    ],
    image_url_xpaths=[
        '//*[@id="img1"]',
        '//*[@id="newsEndContents"]/span[1]/img',
    ],
)

xpaths_dict_106 = dict(
    article_urls_xpath='//*[@id="main_content"]/div[2]/ul/li/dl/dt/a',
    title_xpaths=[
        '//*[@id="content"]/div[1]/div/h2',
        '//*[@id="title_area"]/span',
        '//*[@id="content"]/div/div[1]/div/div[1]/h4',
    ],
    media_xpaths=[
        '//*[@id="content"]/div[1]/div/div[1]/a/img',
        '//*[@id="ct"]/div[1]/div[1]/a/img[1]',
        '//*[@id="pressLogo"]/a/img',
    ],
    content_xpaths=[
        '//*[@id="articeBody"]',
        '//*[@id="dic_area"]',
        '//*[@id="newsEndContents"]',
    ],
    published_xpaths=[
        '//*[@id="content"]/div[1]/div/div[2]/span/em',
        '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span',
        '//*[@id="content"]/div/div[1]/div/div[1]/div/span[1]',
    ],
    image_url_xpaths=[
        '//*[@id="img1"]',
        '//*[@id="newsEndContents"]/span[1]/img',
    ],
)

xpaths_dict_107 = dict(
    article_urls_xpath='//*[@id="main_content"]/div[2]/ul/li/dl/dt/a',
    title_xpaths=[
        '//*[@id="content"]/div/div[1]/div/div[1]/h4',
        '//*[@id="title_area"]/span',
        '//*[@id="content"]/div[1]/div/h2',
    ],
    media_xpaths=[
        '//*[@id="pressLogo"]/a/img',
        '//*[@id="ct"]/div[1]/div[1]/a/img[1]',
        '//*[@id="content"]/div[1]/div/div[1]/a/img',
    ],
    content_xpaths=[
        '//*[@id="newsEndContents"]',
        '//*[@id="dic_area"]',
        '//*[@id="articeBody"]',
    ],
    published_xpaths=[
        '//*[@id="content"]/div/div[1]/div/div[1]/div/span[1]',
        '//*[@id="ct"]/div[1]/div[3]/div[1]/div/span',
        '//*[@id="content"]/div[1]/div/div[2]/span/em',
    ],
    image_url_xpaths=[
        '//*[@id="newsEndContents"]/span[1]/img',
        '//*[@id="img1"]',
    ],
)
