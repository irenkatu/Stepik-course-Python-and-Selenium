from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time, math


link='http://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_id('input_value').text
    
    y=math.log(abs(12*math.sin(int(x))))

    input_element=browser.find_element_by_id('answer')
    input_element.send_keys(str(y))
    check=browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    radiob=browser.find_element_by_css_selector('label[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiob)
    radiob.click()



    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    

finally:
    # 
    time.sleep(10)
    #
    browser.quit()

#