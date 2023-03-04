from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:/Users/jianh/Documents/Web crawler/chromedriver_win32/chromedriver.exe';
driver = webdriver.Chrome(PATH)

# Sction One
# Sample Open the Browser and search keyword in input field
# Open browser
driver.get('https://www.google.com') 

# Write into the txt file
txt = open("website_title.txt", "a")
txt.write("\n" + driver.title)
txt.close()

# print browser title
print(driver.title)

# find the input class or id or name
search = driver.find_element_by_class_name("gLFyf")

# typing the keyword
search.send_keys("facebook")

# keyboard enter
search.send_keys(Keys.RETURN)

# let the pages stop 5 seconds
time.sleep(5)
driver.quit()