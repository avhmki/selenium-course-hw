from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
     
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    
    #def calc(x):
    #    return str(num1 + num2)
        
    y = str(int(num1) + int(num2))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y) 
    
        
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секундR
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
