from selenium import webdriver
import time

try: 
    #link = "http://suninjuly.github.io/registration1.html"
    link ='http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # В ЗАДАНИИ НУЖНЫ ТОЛЬКО ОБЯЗАТЕЛЬНЫЕ!!!
    First = browser.find_element_by_xpath('//div[@class="form-group first_class"]/label[text()="First name*"]/following-sibling::input')
    First.send_keys("Ivan")
    Last = browser.find_element_by_xpath('//div[@class="form-group second_class"]/label[text()="Last name*"]/following-sibling::input')
    Last.send_keys("Petrov")
    Email = browser.find_element_by_xpath('//div[@class="form-group third_class"]/label[text()="Email*"]/following-sibling::input')
    Email.send_keys("yoyoyo@123.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    