from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import bs4

driver = webdriver.Chrome(executable_path='./chromedriver')
url = 'https://mobile.bet365.com/?apptype=&appversion=&cb=1544921750#/AS/B12/'
driver.get(url)
#time.sleep(10)
#elem = driver.find_element_by_class_name("ff-Competitor_Name")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Splash')))
pSource= driver.page_source

soup = bs4.BeautifulSoup(pSource, "html.parser")
for data in soup.findAll(id='Splash'):
    for res in data.find_all('span'):
        print(res.text)
driver.close()
