from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import random
from datetime import datetime, timedelta
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

email_list_file = "email.txt"

with open(email_list_file, "r") as file:
    email_list = [line.strip() for line in file if line.stri()]

def generate_random_date():
    start_date = datetime(1990, 1, 1)
    end_date = datetime(1999, 12, 31)

    days_range = (end_date - start_date).days
    random_days = random.randint(0, days_range)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d %m %Y")

driver.implicitly_wait(10)

def close_pop_up():
    for i in range(1):
        try: 
            
            #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'midasbuy.com/act/pagedoo/')]")))
            WebDriverWait(driver, 3).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@src='https://www.midasbuy.com/act/pagedoo/Activity_1731314030_YUWMUZ/pc/index.html?from=&lan=id&country=id']")))

            # WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'cumulativeRecharge-close')]")))
            close_pop_up_2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "cumulativeRecharge-close_1TD7P")))
            close_pop_up_2.click()
            print("pop up 2 close!")

        except TimeoutException:
            print("gagal close pop up 2 !")
            pass

        driver.switch_to.default_content()

        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[13]')))

            close_pop_up_1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "PatFacePopWrapper_close-btn__erWAb")))
            close_pop_up_1.click()
            print("pop up 1 close!")

        except TimeoutException:
            print("gagal close pop up 1 !")
            pass
        
def log_in():
    driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[2]/div[6]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[4]/div[2]/ul/li[1]/div/div').click()
    time.sleep(0.5)
    try:
        driver.switch_to.frame('login-iframe')
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div/div[3]/div/div/div/div[1]/p/input')))
        input_email.send_keys(email)
        print("Berhasil Input Email !")

    except TimeoutException :
        print("gagal Input Email !")

    driver.find_element(By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div/div[4]/div').click()
    time.sleep(0.5)
    input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/input')))
    input_pass.send_keys(input(f"Input Password : "))
    time.sleep(0.5)

    random_date = generate_random_date()
    print("Tanggal : ", random_date)
    date_input = driver.find_element(By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[4]/div[2]/div[1]/div/input')
    date_input.send_keys(random_date)
    print("tanggal Oke !")
    time.sleep(0.5)

    cek_box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[5]/div[1]/div/div[1]')))
    cek_box.click()

    verif_email =  WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[2]/div')))
    verif_email.click()

try:
    for email in email_list:
        driver.get('https://www.midasbuy.com/midasbuy/id/buy/pubgm')

    close_pop_up()
    log_in()
    print(f"Proses untuk email {email} selesai. Masukkan 'next' Untuk lanjut.")
    while True:
        user_input = input("Input: ").strip().lower()
        if user_input =="next":
            break
        else:
            print("Masukkan 'next' untuk lanjut !")

finally:
    driver.quit()
