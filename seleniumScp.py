from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import bs4

driver = webdriver.Chrome(executable_path='./chromedriver')
url = 'https://mobile.bet365.com/#type=Splash;key=12;ip=0;lng=32'
driver.get(url)
time.sleep(10)
#elem = driver.find_element_by_class_name("ff-Competitor_Name")
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Splash')))
pSource= driver.page_source

soup = bs4.BeautifulSoup(pSource, "html.parser")
print('competitor_name:')
for data in soup.findAll('div',{'class': 'ff-Competitor_Name'}):
    print(data.text)
print('oppName:')
for data in soup.findAll('span',{'class': 'ip-Participant_OppName'}):
    print(data.text)
print('oppOdd:')
for data in soup.findAll('span',{'class': 'ip-Participant_OppOdds'}):
    print(data.text)
driver.close()
