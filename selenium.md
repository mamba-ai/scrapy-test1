
## Selenium Installation
```
pip3 install selenium
>>> Successfully installed selenium-4.1.3
```
### Selenium Documentation
https://www.selenium.dev/documentation/overview/
### Open and close a browser with Selenium
https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/
### Python doc
https://selenium-python.readthedocs.io/locating-elements.html
# Selenium with Edge
```python
driver = webdriver.Edge()
```

### warning
 DeprecationWarning: find_element_by_name is deprecated. Please use find_element(by=By.NAME, value=name) instead

 ### find element by classname
 ```python
item_name = driver.find_element(
    By.CLASS_NAME, "product-intro__head-name").text
 ```

 ### catch NoSuchElementException exception
 ```python
try:
    ...
except selenium.common.exceptions.NoSuchElementException:
    ...
 ```
 ### find buttom and click
有些情况下只有点击之后才能显示内容。
 ```python
descriptions_buttom = driver.find_element(
    By.CLASS_NAME, "product-intro__description-head")
descriptions_buttom.click()
 ```

