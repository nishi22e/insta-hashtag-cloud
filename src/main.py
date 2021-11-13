import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

hashtag = "dog"  # Temporary; need to get user input
driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

time.sleep(3)
driver.quit()
