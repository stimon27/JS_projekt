from selenium import webdriver
from time import sleep
from config import *
import os


def scrape_autocar_articles():

    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.autocar.co.uk/car-news')
    sleep(page_loading_time)

    if driver.find_elements_by_xpath('//button[text()="I Accept"]'):
        driver.find_element_by_xpath('//button[text()="I Accept"]').click()

    article_urls = driver.find_elements_by_xpath('//*[contains(@class, "view-mode-landing_listing_news_first") or contains(@class, "view-mode-landing_listing_news_listing")]/*[@class="details with-image"]/h2/a')
    article_urls = article_urls[:10]
    article_urls = [article_url.get_attribute('href') for article_url in article_urls]

    articles = []

    for article_url in article_urls:
        driver.get(article_url)
        sleep(page_loading_time)

        article_title = driver.find_element_by_xpath('//*[@class="nav-title"]/h1').text
        article_description = driver.find_element_by_xpath('//*[@class="field field-name-field-standfirst field-type-text-long field-label-hidden"]/div/div').text
        article_date = driver.find_element_by_xpath('//*[@class="personality-date" or contains(@class, "block-nodepublished-at")]').text

        article_contents = driver.find_elements_by_tag_name('p')
        article_contents = [p.text for p in article_contents if p.text != '']
        article_contents = " ".join(article_contents)

        articles.append({'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

    driver.quit()
    return articles
