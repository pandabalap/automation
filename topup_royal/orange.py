from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

user_id = "MD1005227"
password = "samakontlo1"

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

def log_in(driver, user_id, password):
    
    input_id = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="IDLoginFrom"]/ul/li[1]/input')))
    input_id.send_keys(user_id)
    print(f"berhasil inpu id")
    time.sleep(1)
    
    input_pass = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="IDLoginFrom"]/ul/li[2]/input')))
    input_pass.send_keys(password)
    print(f"berhasil inpu Password")
    time.sleep(1)
    
    click_login = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/section[3]/a')))
    click_login.click()
    print("Berhasil klik Login !")

def order_item(driver) :
        beli_10b = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[6]/div[3]/div[1]')))
        beli_10b.click()
        print("berhasil klik beli !") 
        time.sleep(1)
        
        masukan_jumlah = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[2]/div[2]/input')))
        masukan_jumlah.send_keys("5")
        print("Jumlah 5 berhasil input !")
        
def klik_pembayaran(driver, pilihan):
    
    if pilihan.lower() == "dana":
        elemen_dana = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[1]')))
        elemen_dana.click()
        print("dana di temukan")
        
    elif pilihan.lower() == "bank":
        elemen_bank = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[2]')))
        elemen_bank.click()
        print("bank di temukan")
        
    elif pilihan.lower() == "qris":
        elemen_qris = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[3]')))
        elemen_qris.click()
        print("qris di temukan")
        
    else:
        print("Pembayaran ora enek Blok !")
    
def konfirmasi(driver):
    
    klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button')))
    klik_beli.click()
    print("berhasil klik tombol beli !")
    time.sleep(1)
    
    klik_tentukan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button[2]')))
    klik_tentukan.click()
    print("berhasil klik tombol Tentukan !")
    time.sleep(12)
    
def close_tab(driver):
    pyautogui.click(567, 68)
    time.sleep(1)
    print("Berhasil close tab !")
    time.sleep(1)
    
    klik_close_reset = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[3]/div/span')))
    klik_close_reset.click()
    print("berhasil klik tombol close Reset !")
    time.sleep(1)
    

    
def hitung_jumlah_order(jumlah_order):
    total = jumlah_order * 10
    return total

def main_process():
    driver = None
    logged_in = False

    try:
        while True:
            try:
                jumlah_order = int(input("Order Piro: "))
                if jumlah_order > 0:
                    break
                else:
                    print("Blok! Lebokno jumlah seng bener.")
            except ValueError:
                print("Salah! Lebokno angka seng bener.")

        pilihan = input("Pembayaranmu opo Ndeng: ")

        if not logged_in:
            driver = create_driver()
            driver.get('http://rd.mitrard.win/MallGoods')

            for i in range(5):
                pyautogui.hotkey('command', '-', interval=0.2)

            time.sleep(1)
            log_in(driver, user_id, password)
            logged_in = True

        while True:
            for i in range(jumlah_order):
                print(f"Proses Order ke-{i + 1}...")
                try:
                    order_item(driver)
                    time.sleep(2)
                    klik_pembayaran(driver, pilihan)
                    time.sleep(2)
                    konfirmasi(driver)
                    time.sleep(2)
                    close_tab(driver)
                    time.sleep(2)
                    driver.refresh()
                    print(f"Order ke-{i + 1} Gacorr !.")
                except Exception as e:
                    print(f"Error order ke-{i + 1}: {e}")
                    break

            user_input = input("Pie Bro? (neh/wes): ").strip().lower()
            if user_input == "neh":
                try:
                    jumlah_order = int(input("Order Piro meneh: "))
                    if jumlah_order > 0:
                        pilihan = input("Pembayaranmu opo Ndeng: ")
                    else:
                        print("Lebokno jumlah seng bener.")
                        continue
                except ValueError:
                    print("Blok ! seng bener cok, ojo ngelamun jorok ")
                    continue
            elif user_input == "wes":
                print("Menutup driver dan keluar.")
                break
            else:
                print("Input Salah. Lebokno 'neh' atau 'wes'.")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main_process()