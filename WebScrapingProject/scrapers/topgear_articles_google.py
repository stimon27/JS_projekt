from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from config import *
import os


def scrape_topgear_articles_google(tags):
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'scrapers/chrome_webdriver/chromedriver.exe'))
    driver.maximize_window()
    sleep(1)

    driver.get('https://www.google.com/')
    sleep(page_loading_time)

    if driver.find_elements_by_id('L2AGLb'):
        driver.find_element_by_id('L2AGLb').click()

    search_query = 'site:topgear.com/car-news'
    for tag in tags:
        search_query += f' AND "{tag}"'

    search_input = driver.find_element_by_name('q')
    search_input.send_keys(search_query)
    sleep(1)

    search_input.send_keys(Keys.RETURN)
    sleep(page_loading_time)

    article_urls = driver.find_elements_by_xpath('//*[@class="g"]/div/div/div/a')

    if article_urls:

        article_urls = [article_url.get_attribute('href') for article_url in article_urls]

        articles = []

        cookies_dialog_passed = False
        newsletter_dialog_passed = False

        for article_url in article_urls:
            driver.get(article_url)
            sleep(page_loading_time)

            if not cookies_dialog_passed:
                if driver.find_elements_by_id('onetrust-accept-btn-handler'):
                    driver.find_element_by_id('onetrust-accept-btn-handler').click()

                cookies_dialog_passed = True

            if not newsletter_dialog_passed:
                if driver.find_elements_by_id('ur-render-target'):
                    driver.switch_to.frame(driver.find_element_by_id('ur-render-target'))
                    reject_button = driver.find_element_by_xpath('//*[@class="buttons"]/*[@class="button reject"]')
                    if reject_button.is_displayed():
                        reject_button.click()
                    driver.switch_to.default_content()
                    newsletter_dialog_passed = True

            article_title = driver.find_element_by_tag_name('h1').text
            article_description = driver.find_element_by_css_selector('h1 + p').text
            article_date = driver.find_elements_by_xpath('//*[@data-testid="Brevier"]')[0].text

            article_contents = driver.find_elements_by_xpath('//*[@data-testid="HtmlContent"]/p')
            article_contents = [p.text for p in article_contents if p.text != '']
            article_contents = " ".join(article_contents)

            articles.append({'article_title': article_title, 'article_description': article_description, 'article_date': article_date, 'article_contents': article_contents})

        driver.quit()
        return articles

    else:
        driver.quit()
        return None
