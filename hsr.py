from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

# 建立驅動器
driver = webdriver.Chrome("chromedriver.exe")

# 開台灣高鐵網頁
driver.get("https://www.thsrc.com.tw/")
driver.maximize_window()

# 點選我同意
driver.find_element(By.CLASS_NAME, "swal2-confirm").click()

# 點上下車地點，並查詢
location1 = driver.find_element(By.ID, 'select_location01')
Select(location1).select_by_visible_text('台北')

location2 = driver.find_element(By.ID, 'select_location02')
Select(location2).select_by_visible_text('台中')

driver.find_element(By.ID, 'start-search').click()

# 抓取出發時間、行車時間、抵達時間、車次、自由座車廂
driver.implicitly_wait(10)  # 最多等 10 秒
rows = driver.find_elements(By.CLASS_NAME, 'tr-row')[:5]
data = []
for row in rows:
    divs = row.find_elements(By.CLASS_NAME, 'tr-td')[:5]
    data.append([div.text for div in divs])

data = pd.DataFrame(data, columns=['出發時間', '行車時間', '抵達時間', '車次', '自由座車廂'])
data