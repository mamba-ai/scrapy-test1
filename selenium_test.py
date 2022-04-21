import selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
# from msedge.selenium_tools import EdgeOptions
# from selenium.webdriver.common.keys import Keys
# print(dir(By))
options = EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get("https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Oversized-Blouse-p-10209809-cat-1733.html")
print(driver.title)

# try:
#     close_window = driver.find_element(
#         By.CLASS_NAME, "S-dialog__closebtn.iconfont-s.icons-Close_12px")
#     close_window.click()
# except selenium.common.exceptions.NoSuchElementException:
#     print("can not find close window")

item_name = driver.find_element(
    By.CLASS_NAME, "product-intro__head-name").text
sku = driver.find_element(
    By.CLASS_NAME, "product-intro__head-sku").text.split(":")[-1]
try:
    price = driver.find_element(
        By.CLASS_NAME, "product-intro__head-price")
    price = price.text.split("¥")[-1]
    price = int("".join(price.split(",")))
except selenium.common.exceptions.NoSuchElementException:
    print("Can not find price")
    price = 0
try:
    color = driver.find_element(
        By.CLASS_NAME, "product-intro__color-title").text.split(":")[-1]
except selenium.common.exceptions.NoSuchElementException:
    print("Can not find color")
    color = "None"

descriptions = {}
try:
    descriptions_buttom = driver.find_element(
        By.CLASS_NAME, "product-intro__description-head")
    descriptions_buttom.click()

    descriptions_table = driver.find_elements(
        By.CLASS_NAME, "product-intro__description-table-item")
    print("table length", len(descriptions_table))
    for des in descriptions_table:
        des_key = des.find_element(
            By.CLASS_NAME, "key").text
        des_val = des.find_element(
            By.CLASS_NAME, "val").text
        descriptions[des_key] = des_val
except selenium.common.exceptions.NoSuchElementException:
    print("Can not find description")
    descriptions = {}

# try:
#     size_buttom = driver.find_element(
#         By.CLASS_NAME, "product-intro__sizeguide-head")
#     size_buttom.click()

#     size_table_head = driver.find_element(
#         By.CLASS_NAME, "cm-inch.common-sizetable__table-tr.trhead")
#     size_table_key = size_table_head.find_elements(
#         By.CLASS_NAME, "td")
#     size_keys = []
#     for k in size_table_key:
#         size_keys.append(k.text)
# except selenium.common.exceptions.NoSuchElementException:
#     print("Can not find size")

print(item_name, sku, price, color, descriptions)
driver.quit()
