from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# print (driver.title)

# search = driver.find_element_by_name("search")
# search.send_keys("Charlotte Hornets")
# search.send_keys(Keys.RETURN)

driver.get("https://en.wikipedia.org/wiki/Charlotte_Hornets")

try:
    tbody = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "td"))
    )
    print(tbody.text)
    
except:
    driver.quit()


driver.quit()
