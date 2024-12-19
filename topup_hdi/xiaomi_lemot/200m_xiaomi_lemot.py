import pyautogui
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

def log_in(user_id, password):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-text'))).click()

    wait.until(EC.visibility_of_element_located((By.ID, 'userId'))).send_keys(user_id)
    wait.until(EC.visibility_of_element_located((By.ID, 'pwd'))).send_keys(password)
    
    wait.until(EC.element_to_be_clickable((By.ID, 'pwdLoginButton'))).click()
    time.sleep(1)
    pyautogui.click(1245,435)
    time.sleep(1)
    
def order_item(jumlah_order):
    for i in range(jumlah_order):
        print(f'Memproses Pesanan Ke-{i + 1}...')
        pyautogui.click(1245,435)
        time.sleep(0.5)
        pyautogui.click(1095, 218)  
        time.sleep(2)
        pyautogui.click(878, 547)    
        time.sleep(1)
        pyautogui.click(1057, 514, 1) 
        time.sleep(1)
        pyautogui.click(892, 706)    
        time.sleep(1)
        pyautogui.click(965, 761)    
        time.sleep(20)
        pyautogui.click(546, 47)     
        time.sleep(1)
        
def hitung_jumlah_order(jumlah_order):
    total = jumlah_order * 25
    return total
        
user_id = input("Masukkan ID: ")
password = "Bajingan123@"
while True:
    try:
        jumlah_order = int(input("Masukkan jumlah Order: "))
        if jumlah_order > 0:
            break
        else:
            print("BLOKK !. Baleni")   
    except ValueError:
        print("Salah !. Masukkan Angka! ")


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)
service = Service('/usr/local/bin/chromedriver') 
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(options=options)
driver.get('https://trade.topbos.com/index.html')
time.sleep(2)

# Perkecil Tampilan
for i in range(5):
    pyautogui.hotkey('command', '-', interval=0.1)

time.sleep(1)

try:
    log_in(user_id,password)
    time.sleep(1)
    
    order_item(jumlah_order)
    total_order = hitung_jumlah_order(jumlah_order)
    print("Order Berhasil ! ", total_order,"M" )
except Exception as e:
    print(f'An error occured: {e}')

driver.quit()
