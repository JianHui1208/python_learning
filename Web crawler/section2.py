from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:/Users/jianh/Documents/Web crawler/chromedriver_win32/chromedriver.exe';

# Section Two
# Record the Instagram Post Text Arae
driver = webdriver.Chrome(PATH)
driver.get('https://www.facebook.com/')

# Waiting The website loading
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "pass"))
)
login = driver.find_element_by_name("login")

# Clear the input field
email.clear()
password.clear()

email.send_keys("***")
password.send_keys("***")
 
login.click()

text_areas = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="jsc_c_d"]/strong/span/a/span/span'))
)
print(text_areas)
text_area_value = driver.find_elements_by_xpath('//*[@id="jsc_c_d"]/strong/span/a/span/span')

txt = open("instragram_textarea.txt", "a")
for text_area in text_area_value:
    txt.write("\n" + text_area.text)

txt.close()