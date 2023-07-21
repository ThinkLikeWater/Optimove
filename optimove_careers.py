from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate
driver.get("https://www.optimove.com/careers")
driver.fullscreen_window()

# Finding and clicking on "Explore more options" button
driver.execute_script("window.scrollBy(0,500)", "")
driver.find_element(by=By.XPATH, value="//*[@class='btn  btn-outline-primary']").click()
# Finding and clicking on "Offices" button
driver.execute_script("window.scrollBy(0, -200)", "")
driver.find_element(by=By.XPATH,
                    value="//div[@class='select select--job-locations']//span[contains(text(), 'All')]").click()
# Selecting Ukraine
driver.find_element(by=By.XPATH,
                    value="//div[@class='selectric-scroll']//li[contains(text(), 'UKR')]").click()
# Checking if there are open QA positions
driver.find_element(by=By.XPATH, value="//div[@class='job-card__title']//a[contains(text(), 'QA Automation Engineer')]")
