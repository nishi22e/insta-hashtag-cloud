import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

hashtag = "dog"  # Temporary; need to get user input
driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

search_bar = driver.find_element_by_class_name("XTCLo")

search_bar.send_keys("hello")
print(search_bar)

# time.sleep(3)
# driver.quit()
