import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

####################### Navigate to Insta#####################

driver_path = "/Users/emilynishikimoto/Desktop/insta-word-cloud/chromedriver"
driver = webdriver.Chrome(driver_path)

hashtag = "#dog"  # Temporary; need to get user input
driver.get(f"https://www.instagram.com/")

########################log in##################################

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
my_username = input("Input your username: \n")
username.send_keys(my_username)

password.clear()
my_password = input("Input your password: \n")
password.send_keys(my_password)

login_button = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

################### Manage Alerts###########################

not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

################# navigate to search bar ###############
search_bar = driver.find_element_by_class_name("XTCLo")
search_bar.send_keys(hashtag)

################### Find 10 most relevant hashtags and their num of posts ########

#key = hashtag, value = num posts
related_hashtags = {}

# for i in range(10):





# print(search_bar)

# time.sleep(3)
# driver.quit()
