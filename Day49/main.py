from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%"
           "20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

email_address = "vedant.pant.100daysofcode@gmail.com"
password = "sigma@123"

time.sleep(5)
sign_in = driver.find_element(By.CLASS_NAME, value="sign-in-modal__outlet-btn")
sign_in.click()

time.sleep(5)
enter_email_address = driver.find_element(By.ID, value='base-sign-in-modal_session_key')
enter_email_address.send_keys(email_address)

time.sleep(5)
enter_password = driver.find_element(By.ID, value='base-sign-in-modal_session_password')
enter_password.send_keys(password)
enter_password.send_keys(Keys.ENTER)

time.sleep(5)
jobs = driver.find_elements(By.CLASS_NAME, value="scaffold-layout__list-container")


for job in jobs:
    print(job.text)
    job.click()
    time.sleep(2)


    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, value='jobs-apply-button')
        easy_apply_button.click()
        time.sleep(2)

        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("7982603081")

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

    time.sleep(5)
    driver.quit()



# time.sleep(5)
# next_button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
# next_button.click()
#
# time.sleep(5)
# next_button_again = driver.find_element(By.XPATH, "//span[text()='Next']/ancestor::button")
# next_button.click()
#
# time.sleep(5)
# work_ex = driver.find_element(By.ID, value="single-line-text-form-component-formElement-urn-li-jobs-"
#                                            "applyformcommon-easyApplyFormElement-4020507370-4218129673-numeric")
# work_ex.send_keys("4")
# work_ex.send_keys(Keys.ENTER)
#
# time.sleep(5)
# review_button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
# review_button.click()
#
# time.sleep(5)
# submit_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
# submit_button.click()






