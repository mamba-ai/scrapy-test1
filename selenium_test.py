from selenium import webdriver
# from msedge.selenium_tools import EdgeOptions
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Oversized-Blouse-p-10209809-cat-1733.html")

driver.quit()
