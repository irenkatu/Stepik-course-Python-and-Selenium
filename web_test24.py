from selenium import webdriver
#from selenium.webdriver.support.ui import Select
import time, math, os


link='http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1=browser.find_element_by_name('firstname')
    input1.send_keys("Marina")
    input2=browser.find_element_by_name('lastname')
    input2.send_keys("Rudina")
    input3=browser.find_element_by_name('email')
    input3.send_keys("Marina@marina.com")

    element=browser.find_element_by_name('file')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test1.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)


    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    # 
    time.sleep(10)
    #
    browser.quit()

#