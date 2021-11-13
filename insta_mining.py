import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

hashtag = "#dog"  # Temporary; need to get user input
driver.get(f"https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
)

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
)

username.clear()
my_username = input("Input your username: \n")
username.send_keys(my_username)

password.clear()
my_password = input("Input your password: \n")
password.send_keys(my_password)

login_button = (
    WebDriverWait(driver, 2)
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    .click()
)

# Manage Alerts

not_now = (
    WebDriverWait(driver, 10)
    .until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    .click()
)

not_now2 = (
    WebDriverWait(driver, 10)
    .until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    .click()
)

search_bar = driver.find_element_by_class_name("XTCLo")
search_bar.send_keys(hashtag)


# key = hashtag, value = num posts
related_hashtags = {}

# for i in range(10):


while True:
    pass
# print(search_bar)

# time.sleep(3)
# driver.quit()
