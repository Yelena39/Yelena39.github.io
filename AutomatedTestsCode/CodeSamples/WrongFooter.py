from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # getting values for calculations
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # selecting the checkbox and the radio button
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    # hiding footer which doesn't let to get to the "Submit" button
    footer = browser.find_element(By.TAG_NAME, "footer")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    button.click()

    # getting the pass code from the alert and printing it into console
    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])

    # this will throw an exception in case the screen size is less than 1600px height
except:
    print("Ooops, seems like your screen is too small...")

finally:
    time.sleep(10)
    browser.quit()
