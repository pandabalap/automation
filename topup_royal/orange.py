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

nomor_dana = "89615140952"

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

def order_item(driver, item, jumlah) :
    xpath_dict = {
        "120m": '//*[@id="app"]/div/div/div[3]/div[1]/div[3]/div[1]',
        "250m": '//*[@id="app"]/div/div/div[3]/div[2]/div[3]/div[1]',
        "500m": '//*[@id="app"]/div/div/div[3]/div[3]/div[3]/div[1]',
        "1b": '//*[@id="app"]/div/div/div[3]/div[4]/div[3]/div[1]',
        "5b": '//*[@id="app"]/div/div/div[3]/div[5]/div[3]/div[1]',
        "10b": '//*[@id="app"]/div/div/div[3]/div[6]/div[3]/div[1]'
    } 
    
    if item not in xpath_dict:
        print(f"Blok ! {item} gak enek.")
        return
    
    item_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_dict[item])))
    item_button.click()
    print(f"{item} berhasil klik !") 
    time.sleep(1)
    
    masukan_jumlah = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[2]/div[2]/input')))
    masukan_jumlah.clear()
    masukan_jumlah.send_keys(jumlah)
    print(f"Jumlah {jumlah} berhasil input untuk {item} !")
        
def klik_pembayaran(driver, pilihan):
    
    if pilihan.lower() == "dana":
        elemen_dana = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[1]')))
        elemen_dana.click()
        print("dana di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button')))
        klik_beli.click()
        print("berhasil klik tombol beli !")
        time.sleep(1)
        
        klik_tentukan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button[2]')))
        klik_tentukan.click()
        print("berhasil klik tombol Tentukan !")
        time.sleep(8)
        
        #klik konfirmasi
        pyautogui.click(600, 910)
        time.sleep(2)
        
        #klik input dana
        pyautogui.click(710, 510)
        time.sleep(2)
        
        #tulis no dana
        pyautogui.write(nomor_dana)
        time.sleep(5)
        
        #klik Continue
        pyautogui.click(750, 865)
        time.sleep(20)
        
        #close tab dana
        pyautogui.click(805, 67)
        time.sleep(2)
        
        
    elif pilihan.lower() == "bank":
        elemen_bank = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[2]')))
        elemen_bank.click()
        print("bank di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button')))
        klik_beli.click()
        print("berhasil klik tombol beli !")
        time.sleep(1)
        
        klik_tentukan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button[2]')))
        klik_tentukan.click()
        print("berhasil klik tombol Tentukan !")  
        time.sleep(6)
        
        #klik konfirmasi
        pyautogui.click(600, 910)
        time.sleep(2)
        
        #salin/copy
        pyautogui.click(755, 500)
        time.sleep(20)
        
    elif pilihan.lower() == "qris":
        elemen_qris = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[1]/div[6]/div[3]')))
        elemen_qris.click()
        print("qris di temukan")
        
        klik_beli = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button')))
        klik_beli.click()
        print("berhasil klik tombol beli !")
        time.sleep(1)
        
        klik_tentukan = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[1]/div[3]/button[2]')))
        klik_tentukan.click()
        print("berhasil klik tombol Tentukan !")
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
    
    
def close_tab(driver):
    pyautogui.click(567, 68)
    time.sleep(0.8)
    print("Berhasil close tab !")
    
    klik_close_reset = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By. XPATH, '//*[@id="app"]/div/div/div[3]/div[10]/div[3]/div/span')))
    klik_close_reset.click()
    print("berhasil klik tombol close Reset !")
    time.sleep(0.5)
    

    
def hitung_jumlah_order(jumlah_order):
    isi_per_item = {
        ""
    }

def main_process():
    driver = None
    logged_in = False
    
    jumlah_dict = {
                    "120m": 100,
                    "250m": 100,
                    "500m": 100,
                    "1b": 50,
                    "5b": 10,
                    "10b": 5
                }

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
                
            while True:
                if item not in jumlah_dict:
                    print("denom gak enk blok !")
                    continue
                
        item = input("Masukkan Denom : ").strip()
        pilihan = input("Pembayaranmu opo ? : ")

        if not logged_in:
            driver = create_driver()
            driver.get('http://rd.mitrard.win/MallGoods')
            
            driver.execute_script("document.body.style.zoom='50%'")
            time.sleep(0.5)
            # for i in range(5):
            #     pyautogui.hotkey('command', '-', interval=0.2)

            log_in(driver, user_id, password)
            logged_in = True
            time.sleep(1)

        while True:
            for i in range(jumlah_order):
                print(f"Proses Order ke-{i + 1}...")
                try:
                    # Untuk Zoom Out
                    driver.execute_script("document.body.style.zoom='50%'")
                    time.sleep(0.5)
                    
                    order_item(driver, item, jumlah_dict[item])
                    time.sleep(0.8)
                    klik_pembayaran(driver, pilihan)
                    time.sleep(0.8)
                    close_tab(driver)
                    time.sleep(0.8)
                    driver.refresh()
                    print(f"Order ke-{i + 1} Gacorr !.")
                except Exception as e:
                    print(f"Error order ke-{i + 1}: {e}")
                    break

            user_input = input("Pie Bro? neh/wes: ").strip().lower()
            if user_input == "neh":
                try:
                    jumlah_order = int(input("Order Piro meneh: "))
                    if jumlah_order > 0:
                        item = input("Masukkan Denom : ").strip()
                        pilihan = input("Pembayaranmu opo ? : ")
                    else:
                        print("Lebokno jumlah seng bener.")
                        continue
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
    main_process()