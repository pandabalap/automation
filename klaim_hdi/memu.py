from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import time

# Konfigurasi Desired Capabilities untuk emulator Memu
desired_caps = {
    "platformName": "Android",       # Platform yang digunakan
    "deviceName": "Android Device",   # Nama perangkat emulator
    "appPackage": "com.neptune.dominogl",  # Ganti dengan package aplikasi yang dituju
    "appActivity": "com.pokercity.lobby.lobby",   # Ganti dengan activity utama aplikasi
    "udid": "127.0.0.1:26625",
    "automationName": "UiAutomator2",
    "noReset": True                   # Tidak mengatur ulang data aplikasi
}

# Membuat koneksi ke Appium Server
driver = webdriver.Remote("http://localhost:4723", desired_caps)

driver.implicitly_wait(10)

# Koordinat untuk mengklik (contoh klik inbox pada game)
klik_inbox = {"x" : 970 ,"y": 825}
klik_refresh = {"x" : 420 ,"y": 740}
klik_mail = {"x" : 330 ,"y": 230}
klik_receive = {"x" : 1005 ,"y": 735}
klik_confirm = {"x" : 800 ,"y": 705}
klik_exit = {"x" : 1520 ,"y": 195}



actions = ActionChains(driver)

def proses_awal():
    print("Proses awal berjalan...")

    actions.w3c_actions.pointer_action.move_to_location(klik_inbox["x"],klik_inbox["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_refresh["x"],klik_refresh["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    
    actions.w3c_actions.pointer_action.move_to_location(klik_mail["x"],klik_mail["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_receive["x"],klik_receive["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_confirm["x"],klik_confirm["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_exit["x"],klik_exit["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    
def proses_dua():
    print("Proses kedua tanpa Refres berjalan...")
        
    actions.w3c_actions.pointer_action.move_to_location(klik_inbox["x"],klik_inbox["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    
    actions.w3c_actions.pointer_action.move_to_location(klik_mail["x"],klik_mail["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_receive["x"],klik_receive["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_confirm["x"],klik_confirm["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)
    
    actions.w3c_actions.pointer_action.move_to_location(klik_exit["x"],klik_exit["y"])
    actions.w3c_actions.pointer_action.click()
    actions.perform()
    time.sleep(1)

def main_proses():
    try:    
        while True:
            try :
                jumlah_klaim = int(input("Masukkan jumlah : "))
                if jumlah_klaim > 0:
                    break
                else:
                    print("ulangi !")
                    
            except ValueError :
                print("Salah blok, masukkan angka ")
            
        proses_awal()
        while True:    
            for i in range(jumlah_klaim):
                print(f"Proses klaim ke-{i + 1}...")
                try:
                    proses_dua()
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Error order ke-{i + 1}: {e}")
                    
            print("Klaim Sukses All !")
            break
         
    finally:
        if driver:
            driver.quit()
        
if __name__ == "__main__":
    main_proses()
