from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ozon.ru")
elem = driver.title
print(elem)
assert "No results found." not in driver.page_source
driver.close()
