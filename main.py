import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from lxml import html

driver = Chrome(executable_path='chromedriver.exe')
driver.get('https://whocutie.aliexpress.com/store/all-wholesale-products/2996039.html?spm=a2g0o.store_pc_home" \
      ".pcShopHead_6241067.99')


# URL = "https://whocutie.aliexpress.com/store/all-wholesale-products/2996039.html?spm=a2g0o.store_pc_home" \
#       ".pcShopHead_6241067.99"
# response = requests.get(URL)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# h3_titles = soup.findAll('li')
#
# for title in h3_titles:
#     print(title)