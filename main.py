from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

'''
Constants
'''
WEBDRIVER_PATH = "chromedriver_win32/chromedriver.exe"
LOGIN_URL = ''
LOGIN_X_PATH=''
LOGIN_ID = ''
LOGIN_PW = ''
FILENAME = ''

'''
Options
'''
options = Options()
options.add_argument('--headless') # browser invisible
options.add_argument('--no-sandbox')
# options.add_argument('window-size=1920x1080') # set window size
options.add_argument("disable-gpu") # 그래픽 가속 비활성화
options.add_argument("lang=ko_KR") # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36') # user-agent 이름 설정

'''
Run
'''
driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)
# Login
driver.implicitly_wait(3)
driver.get(LOGIN_URL)
driver.find_element(By.NAME, 'uEmail').send_keys(LOGIN_ID)
driver.find_element(By.NAME, 'uPwd').send_keys(LOGIN_PW)
driver.find_element(By.XPATH, LOGIN_X_PATH).click()
# Move to productManage page
driver.find_element(By.ID, 'topmenu4').click()
# Move to series product list page
driver.execute_script("fncGoProductSearch('SERIESE')")
# Get titles
table_head = driver.find_element(By.TAG_NAME, 'thead')
title_rows = table_head.find_elements(By.TAG_NAME, 'th')
titles = []
for row in title_rows:
    title_row = row.text
    title_row = title_row.replace('\n', ' ')
    titles.append(title_row)
# Get values
values = []
i = 0
while True:
    driver.execute_script(f"fncMovePage('{i}')")
    time.sleep(0.2) # Because of script execute time
    value_rows = driver.find_elements(By.CLASS_NAME, 'trType01')
    if not value_rows: # Break if page is not exist
        break
    for row in value_rows:
        temp = []
        tds = row.find_elements(By.TAG_NAME, 'td')
        for td in tds:
            td_d = td.text
            temp.append(td_d)
        values.append(temp)
    i += 10

'''
Save
'''
f = open(FILENAME, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

writer.writerow(titles)
for value in values:
    writer.writerow(value)