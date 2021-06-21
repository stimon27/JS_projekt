from selenium import webdriver
from time import sleep
from config import *
import os


def scrape_motor1_articles():
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.motor1.com/news/')
    sleep(page_loading_time)

    if driver.find_elements_by_id('onetrust-accept-btn-handler'):
        driver.find_element_by_id('onetrust-accept-btn-handler').click()

    driver.execute_script("window.scrollTo(0, 2000)")
    article_urls = driver.find_elements_by_xpath('//*[@class="browseBox detailed-box browseBox-half"]/*[contains(@class, "item")]/a')
    article_urls = article_urls[:10]
    article_urls = [article_url.get_attribute('href') for article_url in article_urls]

    articles = []

    for article_url in article_urls:
        driver.get(article_url)
        sleep(page_loading_time)

        article_title = driver.find_element_by_tag_name('h1').text
        article_description = driver.find_element_by_xpath('//h2[@class="preview"]').text
        article_date = driver.find_element_by_xpath('//*[@class="date-data"]').text

        article_contents = driver.find_elements_by_xpath('//*[@class="postBody description e-content"]/p')
        article_contents = [p.text for p in article_contents if p.text != '']
        article_contents = " ".join(article_contents)

        articles.append(
            {'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

    driver.quit()
    return articles

