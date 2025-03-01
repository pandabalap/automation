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


def create_driver():
    options = webdriver.ChromeOptions() 
    options.add_experimental_option('detach', True) 
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

# read file email
def read_email_list(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# buat tanggal rendom
def generate_random_date():
    start_date = datetime(1990, 1, 1)
    end_date = datetime(1999, 12, 31)

    days_range = (end_date - start_date).days
    random_days = random.randint(0, days_range)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d %m %Y")



def close_pop_up(driver):
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
        
def log_in(driver, email):
    try:
        #klik masuk
        driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[2]/div[4]').click()
        time.sleep(0.5)
        
        # #klik log_in/daftar
        # driver.find_element(By.XPATH, '//*[@id="MobileNav"]/div/div[4]/div[2]/ul/li[1]/div/div').click()
        # time.sleep(0.5)
        driver.switch_to.frame('login-iframe')

        #masukkan email
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div/div[3]/div/div/div/div[1]/p/input')))
        input_email.send_keys(email)
        print(f"Berhasil Input Email {email} !")

        #klik tombol lanjut
        driver.find_element(By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div/div[4]/div').click()
        time.sleep(0.5)

        #masukkan password
        input_pass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div/input')))
        # input_pass.send_keys(input(f"Input Password : "))
        input_pass.send_keys("Jembutasu123@")
        time.sleep(0.5)

        #masukkan random tanggal 
        random_date = generate_random_date()
        print("Tanggal : ", random_date)
        date_input = driver.find_element(By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/div/input')
        date_input.send_keys(random_date)
        print("tanggal Oke !")
        time.sleep(0.5)

        #cek list box konfirmasi syarat
        cek_box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[1]/div[5]/div[1]/div/div[1]')))
        cek_box.click()

        #klik tombol verif email
        verif_email =  WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-sdk-app"]/div[1]/div/div[3]/div[1]/div[2]/div')))
        verif_email.click()
        print(f"Gass Verif di {email} Ibox")

    except TimeoutException :
        print(" Log in dan Input Email Gagal !")


def main_prosess(email_list_file):
    email_list = read_email_list(email_list_file)
    email_index = 0

    # perulangan email dan Worker
    while email_index < len(email_list):
        email = email_list[email_index]
        driver = create_driver()
        try: 
            driver.get('https://www.midasbuy.com/midasbuy/id/buy/pubgm')
            close_pop_up(driver)
            log_in(driver, email)
        except Exception as e:
            print(f"An Error Occured: {e}")
        finally:
            print(f"Proses untuk email {email} selesai. Lebokno 'neh' kango lanjut.")
            while True:
                user_input = input("Njalukmu opo cok : ").strip().lower()
                if user_input =="neh":
                    driver.quit()
                    email_index += 1
                    break

                elif user_input =="wes":
                    driver.quit()
                    print("proses dihentikan")
                    return
                else:
                    print("Lebokno 'neh' kango lanjut nek 'wes' kango mandek !")

    print("EMAIL ENTEK COK ! SESUK NEH !")

# jalankan worker berdasarkan jumlah email
if __name__ == "__main__":
        email_list_file = "email.txt"
        main_prosess(email_list_file)


