from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立驅動器
driver = webdriver.Chrome('chromedriver.exe') 

# 開網頁
driver.get("https://www.google.com")

# 搜尋
search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
search.send_keys('遊戲天堂')
search.send_keys(Keys.RETURN)

# 關網頁
# driver.quit()