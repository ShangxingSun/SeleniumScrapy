from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import bs4
import json

driver = webdriver.Chrome(executable_path='./chromedriver')
url = 'https://mobile.bet365.com/#type=Splash;key=12;ip=0;lng=32'
driver.get(url)
time.sleep(5)
# elem = driver.find_element_by_class_name("ff-Competitor_Name")
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Splash')))
pSource = driver.page_source

soup = bs4.BeautifulSoup(pSource, "html.parser")
x = {
    'competitor': [],
    'oppName': [],
    'oppOdd': []
}
# print('competitor_name:')
for data in soup.findAll('div', {'class': 'ff-Competitor_Name'}):
    x['competitor'].append(data.text)
# print('oppName:')
for data in soup.findAll('span', {'class': 'ip-Participant_OppName'}):
    x['oppName'].append(data.text)
# print('oppOdd:')
for data in soup.findAll('span', {'class': 'ip-Participant_OppOdds'}):
    x['oppOdd'].append(data.text)
y = json.dumps(x)
print(y)
driver.close()
