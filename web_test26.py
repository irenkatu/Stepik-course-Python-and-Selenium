from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time, math, os


link='http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x=browser.find_element_by_id('input_value').text
    y=math.log(abs(12*math.sin(int(x))))
    answer=browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    # 
    time.sleep(10)
    #
    browser.quit()

#