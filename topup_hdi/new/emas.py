from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import pyautogui
import time


user_id = input("Masukkan ID: ")
password = "Bajingan123@"

nomor_dana = "89615140952"

def create_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def log_in(driver, user_id, password):
    wait = WebDriverWait(driver, 3)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-text'))).click()

    wait.until(EC.visibility_of_element_located((By.ID, 'userId'))).send_keys(user_id)
    
    wait.until(EC.visibility_of_element_located((By.ID, 'pwd'))).send_keys(password)

    wait.until(EC.element_to_be_clickable((By.ID, 'pwdLoginButton'))).click()
    time.sleep(1)
    #klik layar
    print("berhasil login !")
    
    klik_topup = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div/header/div/ul/li[2]/a')))
    klik_topup.click()
    print("berhasil klik_topup")
    
    # pyautogui.click(1245,435)
    time.sleep(2)
    
def order_item(driver, item, jumlah_klik) :
    xpath_dict = {
        "1m": '/html/body/section/div[1]/article[1]/div/aside/div/ul/li[1]',
        "60m": '/html/body/section/div[1]/article[1]/div/aside/div/ul/li[2]',
        "200m": '/html/body/section/div[1]/article[1]/div/aside/div/ul/li[3]',
        "1b": '/html/body/section/div[1]/article[1]/div/aside/div/ul/li[5]'
    } 
    
    if item not in xpath_dict:
        print(f"Blok ! {item} gak enek.")
        return
    item_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_dict[item])))
    item_button.click()
    print(f"berhasil klik Denom {item} !") 
    time.sleep(1)
    
    for _ in range(jumlah_klik):
        klik_jumlah = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buyItem"]/aside/div/div/a[2]')))
        klik_jumlah.click()
        time.sleep(0.5)
        
    print(f"Berhasil klik {jumlah_klik} kali untuk Denom {item}!")
    
def klik_pembayaran(driver, pilihan):
    
    if pilihan.lower() == "dana":
        elemen_dana = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buyItem"]/aside/ul/li[1]')))
        elemen_dana.click()
        print("dana di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="buyItem"]/aside/a')))
        klik_beli.click()
        print("berhasil klik tombol Top up !")
        time.sleep(1)
        
        #klik input dana
        pyautogui.click(600, 445)
        time.sleep(2)
        
        #tulis no dana
        pyautogui.write(nomor_dana)
        time.sleep(5)
        
        #klik Continue
        pyautogui.click(660, 780)
        time.sleep(20)
        
        
    elif pilihan.lower() == "ovo":
        elemen_bank = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buyItem"]/aside/ul/li[2]')))
        elemen_bank.click()
        print("bank di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="buyItem"]/aside/a')))
        klik_beli.click()
        print("berhasil klik tombol Top up !")
        
        time.sleep(20)
        
    elif pilihan.lower() == "bank":
        elemen_bank = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buyItem"]/aside/ul/li[5]')))
        elemen_bank.click()
        print("bank di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="buyItem"]/aside/a')))
        klik_beli.click()
        print("berhasil klik tombol Top up !")
        
        time.sleep(20)
        
        
    elif pilihan.lower() == "qris":
        elemen_qris = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="buyItem"]/aside/ul/li[4]')))
        elemen_qris.click()
        print("qris di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="buyItem"]/aside/a')))
        klik_beli.click()
        print("berhasil klik tombol Top up !")
    
        time.sleep(12)
        
        # tabs = driver.window_handles
        # print("Semua Tab yang Terbuka: ", tabs)
        # driver.switch_to.window(tabs[-1])  # Pindah ke tab baru
        # print("Berhasil pindah tab baru")
        # time.sleep(2)
        
        # gambar = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//div(@class="van-button__content")')))
        # gambar.click()
        # print(" qris unduh")
        
        # driver.close(tabs[-1])
        # print("Berhasil close tab baru")
        
        # driver.switch_to.window(tabs[0])
        # print("Berhasil pindah tab lama")
        
    else:
        print("Pembayaran ora enek Blok !")
        
def close_tab():
    pyautogui.click(567, 68)
    time.sleep(0.8)
    print("Berhasil close tab !")
    
def hitung_jumlah_order(item, jumlah_order):
    isi_per_item = {
        "1m": 500,
        "60m": 50,
        "200m": 25,
        "1b": 5
    }

    # Periksa apakah item valid
    if item not in isi_per_item:
        print(f"Item '{item}' tidak valid!")
        return None
    
    total = isi_per_item[item] * jumlah_order
    return total

def main_proses():
    driver = None
    logged_in = False
    
    try:
        jumlah_order = int(input("Order Piro: "))
        while True:
            item = input("Masukkan Denom : ").strip()
            if item in ["1m", "60m", "200m", "1b"]:
                break
            print("Blok! Denom gak enek.")
            
        pilihan = input("Pembayaranmu opo ? : ")
        
        if not logged_in:
            driver = create_driver()
            driver.get('https://trade.topbos.com/index.html')
            
            # Untuk Zoom Out
            driver.execute_script("document.body.style.zoom='50%'")
            time.sleep(0.5)
            # for i in range(5):
            #     pyautogui.hotkey('command', '-', interval=0.2)
                    
            time.sleep(1)
            log_in(driver, user_id, password)
            logged_in = True
            
        while True:
            for i in range(jumlah_order):
                print(f"Proses Order ke-{i + 1}...")
                try:
                    order_item(driver, item, jumlah_klik=5)
                    time.sleep(0.8)
                    klik_pembayaran(driver, pilihan)
                    time.sleep(0.8)
                    close_tab()
                    time.sleep(0.8)
                    driver.refresh()
                    total_order = hitung_jumlah_order(item, jumlah_order)
                    print(f"Order ke-{i + 1} Gacorr !.")
                    print("Order Berhasil !", total_order,"B" )
                except Exception as e:
                    print(f"Error order ke-{i + 1}: {e}")
                    break
                
            user_input = input("Pie Bro? neh/wes: ").strip().lower()
            if user_input == "neh":
                try:
                    jumlah_order = int(input("Order Piro Meneh ? : "))
                    item = input("Masukkan Denom : ").strip()
                    pilihan = input("Pembayaranmu opo ? : ")
                except ValueError:
                    print("Blok ! seng bener cok, ojo ngelamun jorok ")
                    continue
            elif user_input == "wes":
                print("Matur Suwun Sek. Agus nih Boss. TAMPLING Dong. Muahh ")
                break
            else:
                print("Input Salah. Lebokno 'neh' atau 'wes'.")
    finally:
        if driver:
            driver.quit()
    
if __name__ == "__main__":
    main_proses()
 
