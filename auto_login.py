#baris-ertas

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


mail = "*" #e-mail address here
mailPw = "*" #e-mail password here
driver = webdriver.Chrome('/Users/barisertas/Downloads/chromedriver-2') #path of the chrome-driver
url = "https://webmail.bilkent.edu.tr/" # you replace any url you want.
driver.get(url) #opens the url

#html tags and getting them
pw = '[id^="LoginForm-"]'
driver.find_element_by_id("rcmloginuser").send_keys(mail)
pas = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, pw)))
pas.send_keys(mailPw)
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"rcmloginsubmit")))
button.click() #triggers login button

