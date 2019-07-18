import urllib
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class PubMedInfo():
    def __init__(self, KeywordList):
        print("fsad")
        self.counter = 0
        self.target_urls = []
        self.start_url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
        self.base_url = 'https://www.ncbi.nlm.nih.gov'
        self.temp = [urllib.parse.quote(i) for i in keywordlist]
        self.keyword = '%2C'.join(self.temp)
        self.url = self.start_url + self.keyword
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(browser, 10)

    def page_size_click(self):
        perpage = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@class="inline_list left display_settings"]/li[3]/a/span[4]')))
        perpage.click()
        page_200 = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#display_settings_menu_ps > fieldset > ul > li:nth-child(6) > label')))
        page_200.click()

    def next_page():
        try:
            self.nextpage = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Next page of results"]')))
        except TimeoutException:
            self.next_page()

    def get_target_urls(self):
        html = self.browser.page_source
        soup = BeautifulSoup(html, "html5lib")
        for link in soup.find_all('a'):
            if(link.get('href') is not None and  len(link.get('href')) > 10 and link.get('href')[:10] == '/pubmed/31'): 
                self.target_urls.append(link.get('href')) 

    def gethtmltext(url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = 'utf-8'
            return r.text
        except:
            return ""

    def fillfile(html, soup, url):
        try:
            with open(str(self.counter) + ". " + soup.find_all('h1')[1].get_text() + '.txt', 'w+') as f:
                f.write(soup.find('div', 'abstr').get_text()[8:])
            print(soup.find_all('h1')[1].get_text())
        except:
            pass

    def get_abstract(self):
        for link in self.target_urls:
            real_url = self.base_url + link
            html = self.gethtmltext(real_url)
            soup = BeautifulSoup(html, "html5lib")
            fillfile(html, soup, url)

    def main():
        self.page_size_click()
        self.get_target_urls()
        self.next_page()

if __name__ == '__main__':
    a = PubMedInfo(['TCGA', 'breast', 'cancer'])
    a.main()