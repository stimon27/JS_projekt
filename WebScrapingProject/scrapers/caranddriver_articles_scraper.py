from selenium import webdriver
from time import sleep
from config import *
import os


def scrape_caranddriver_articles():
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.caranddriver.com/news/')
    sleep(page_loading_time)

    if driver.find_elements_by_id('onetrust-accept-btn-handler'):
        driver.find_element_by_id('onetrust-accept-btn-handler').click()

    article_urls = driver.find_elements_by_xpath('//*[contains(@class, "full-item")]/a')
    article_urls = article_urls[:10]
    article_urls = [article_url.get_attribute('href') for article_url in article_urls]

    driver.refresh()
    sleep(page_loading_time)

    articles = []

    for article_url in article_urls:

        driver.get(article_url)
        sleep(page_loading_time)

        article_title = driver.find_element_by_xpath('//*[contains(@class, "content-hed")]').text
        article_description = driver.find_element_by_xpath('//*[contains(@class, "content-dek")]/p').text
        article_date = driver.find_element_by_xpath('//*[@class="content-info-date"]').text

        article_contents = driver.find_elements_by_xpath('//*[@class="body-text"]')
        article_contents = [article_content.text for article_content in article_contents]
        article_contents = " ".join(article_contents)

        articles.append({'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

    driver.quit()
    return articles
