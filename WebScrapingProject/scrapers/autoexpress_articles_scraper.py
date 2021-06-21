from selenium import webdriver
from time import sleep
from config import *
import os


def scrape_autoexpress_articles():
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.autoexpress.co.uk/car-news')
    sleep(page_loading_time)

    driver.switch_to.frame(driver.find_element_by_id('sp_message_iframe_391602'))

    if driver.find_elements_by_xpath('//button[@title="ACCEPT ALL"]'):
        driver.find_element_by_xpath('//button[@title="ACCEPT ALL"]').click()

    sleep(3)
    driver.switch_to.default_content()


    article_urls = driver.find_elements_by_xpath('//*[@class="polaris__link polaris__article-card--link"]')
    article_urls = article_urls[:10]
    article_urls = [article_url.get_attribute('href') for article_url in article_urls]

    articles = []

    for article_url in article_urls:
        driver.get(article_url)
        sleep(page_loading_time)

        article_title = driver.find_element_by_tag_name('h1').text
        article_description = driver.find_element_by_xpath('//*[contains(@class, "-content-subtitle")]').text
        article_date = driver.find_elements_by_xpath('//*[@class="polaris__date"]')[0].text

        article_contents = driver.find_elements_by_xpath('//*[@class="polaris__simple-grid--main"]/p')
        article_contents = [p.text for p in article_contents if p.text != '']
        article_contents = " ".join(article_contents)

        articles.append({'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

    driver.quit()
    return articles
