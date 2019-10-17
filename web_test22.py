from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math


link='http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    x=browser.find_element_by_id('num1').text
    y=browser.find_element_by_id('num2').text
    z=str(int(x)+int(y))
    selection = Select(browser.find_element_by_tag_name("select"))
    selection.select_by_value(z)


    button = browser.find_element_by_css_selector('.btn-default')
    button.click()

    

finally:
    # 
    time.sleep(10)
    #
    browser.quit()

#