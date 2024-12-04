from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

def close_pop_up():
    for i in range(1):
        driver.get('https://www.midasbuy.com/midasbuy/id/buy/pubgm')

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[13]')))
            print("pop up muncul!")

            driver.find_element(By.CLASS_NAME, "PatFacePopWrapper_close-btn__erWAb").click()
            print("pop up close!")

        except TimeoutException:
            print("gagal close pop up!")
            pass
def log_in():
    driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[2]/div[6]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[4]/div[2]/ul/li[1]/div/div').click()
    time.sleep(0.5)
    try:
        driver.switch_to.frame('login-iframe')
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div/div[3]/div/div/div/div[1]/p/input')))
        input_email.send_keys(input(f"Input Email : "))
        print("Berhasil Input Email !")

    except TimeoutException :
        print("gagal Input Email !")

    driver.find_element(By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div/div[4]/div').click()
    time.sleep(0.5)
    input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/input')))
    input_pass.send_keys(input(f"Input Password : "))
    time.sleep(0.5)


close_pop_up()
log_in()
