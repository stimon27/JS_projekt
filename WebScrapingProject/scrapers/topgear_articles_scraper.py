from selenium import webdriver
from time import sleep
from config import *
import os


def scrape_topgear_articles():
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.topgear.com/car-news')
    sleep(page_loading_time)

    if driver.find_elements_by_id('onetrust-accept-btn-handler'):
        driver.find_element_by_id('onetrust-accept-btn-handler').click()

    articles = []

    index = 0
    while index < 10:

        driver.get('https://www.topgear.com/car-news')
        sleep(page_loading_time)

        if driver.find_elements_by_id('ur-render-target'):
            driver.switch_to.frame(driver.find_element_by_id('ur-render-target'))
            reject_button = driver.find_element_by_xpath('//*[@class="buttons"]/*[@class="button reject"]')
            if reject_button.is_displayed():
                reject_button.click()
            driver.switch_to.default_content()

        article_headers = driver.find_elements_by_xpath('//*[contains(@class, "card-header")]')
        article_headers[index].click()
        sleep(page_loading_time)

        if driver.find_elements_by_id('ur-render-target'):
            driver.switch_to.frame(driver.find_element_by_id('ur-render-target'))
            reject_button = driver.find_element_by_xpath('//*[@class="buttons"]/*[@class="button reject"]')
            if reject_button.is_displayed():
                reject_button.click()
            driver.switch_to.default_content()

        article_title = driver.find_element_by_tag_name('h1').text
        article_description = driver.find_element_by_css_selector('h1 + p').text
        article_date = driver.find_elements_by_xpath('//*[@data-testid="Brevier"]')[0].text

        article_contents = driver.find_elements_by_xpath('//*[@data-testid="HtmlContent"]/p')
        article_contents = [p.text for p in article_contents if p.text != '']
        article_contents = " ".join(article_contents)

        articles.append({'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

        index += 1

    driver.quit()
    return articles

