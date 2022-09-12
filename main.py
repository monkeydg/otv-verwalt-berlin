import time
from datetime import datetime
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def play_alarm():
            for i in range(0, 3):
                winsound.Beep(600, 1000)
                winsound.Beep(800, 1000)

while True:
    dt_string = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(30) # seconds
        driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")
        assert "book appointment" in driver.title

        # PAGE 1
        book_link = driver.find_element(By.LINK_TEXT, 'Book Appointment')
        book_link.click()

        # PAGE 2
        tickbox = driver.find_element(By.ID, 'xi-cb-1')
        tickbox.click()
        next_button = driver.find_element(By.ID, "applicationForm:managedForm:proceed")
        next_button.click()

        # PAGE 3
        citizenship = driver.find_element(By.ID, 'xi-sel-400')
        citizenship.click()
        time.sleep(2)
        citizenship.send_keys("Lebanon")
        citizenship.send_keys(Keys.RETURN)

        num_applicants = driver.find_element(By.ID, 'xi-sel-422')
        num_applicants.click()
        time.sleep(2)
        num_applicants.send_keys("one person")
        num_applicants.send_keys(Keys.RETURN)

        family = driver.find_element(By.ID, 'xi-sel-427')
        family.click()
        time.sleep(2)
        family.send_keys("no")
        family.send_keys(Keys.RETURN)

        application_type = driver.find_element(By.CSS_SELECTOR, "#xi-div-30 > div.ozg-kachel.kachel-451-0-1.level1 > label")
        application_type.click()

        application_purpose = driver.find_element(By.CSS_SELECTOR, "#inner-451-0-1 > div > div.ozg-accordion.accordion-451-0-1-3.level2 > label")
        application_purpose.click()

        studying_permit = driver.find_element(By.CSS_SELECTOR, "#inner-451-0-1 > div > div:nth-child(2) > div > div:nth-child(4) > label")
        studying_permit.click()

        time.sleep(5)
        finish_button = driver.find_element(By.CSS_SELECTOR, '#applicationForm\:managedForm\:proceed')
        finish_button.click()

        # PAGE 4
        time.sleep(30)
        assert "Service selection" in driver.title
        if "There are currently no dates available for the selected service!" in driver.page_source:
            driver.save_screenshot(f'logs_neg/{dt_string}.png')
            driver.close()
        else:
            driver.save_screenshot(f'logs_pos/{dt_string}.png')
            play_alarm()
            while True:
                time.sleep(10000)
    except:
        driver.save_screenshot(f'logs_err/{dt_string}.png')
        driver.close()