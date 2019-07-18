from selenium import webdriver
import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))
browser.find_element_by_css_selector('#book').click()

valel = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "input_value")))
val = calc(int(valel.text))
browser.find_element_by_css_selector('#answer').send_keys(val)

browser.find_element_by_css_selector('#solve').click()
