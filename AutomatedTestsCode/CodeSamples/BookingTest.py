from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Selenium is checking for 12 seconds if the price of the booking is $100
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()

    # getting values for calculations
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # scrolling into view to enter the answer
    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button1 = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    button1.click()

    # checking if the alert has certain message otherwise indicating that the test has failed
    alert = browser.switch_to.alert
    assert "Congrats, you've passed the task!" in alert.text, "Test has failed"
    
    # getting the pass code from the alert and printing it into console
    print(alert.text.split(': ')[-1])

    time.sleep(7)
    alert.accept()

finally:

    time.sleep(10)
    browser.quit()