from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import time
import configparser
import threading

# Koordinat untuk mengklik (contoh klik inbox pada game)
klik_inbox = {"x" : 970 ,"y": 825}
klik_refresh = {"x" : 420 ,"y": 740}
klik_mail = {"x" : 330 ,"y": 230}
klik_receive = {"x" : 1005 ,"y": 735}
klik_confirm = {"x" : 800 ,"y": 705}
klik_exit = {"x" : 1520 ,"y": 195}

def run_automation(section):
    config = configparser.ConfigParser()
    config.read("config.cfg")
    
    devicename = config.get(section, "devicename")
    udid = config.get(section, "udid")
    remote_url = config.get(section, "remote_url")
    
    
    # Konfigurasi Desired Capabilities untuk emulator Memu
    desired_caps = {
        "platformName": "Android",       # Platform yang digunakan
        "deviceName": devicename,   # Nama perangkat emulator
        "appPackage": "com.neptune.dominogl",  # Ganti dengan package aplikasi yang dituju
        "appActivity": "com.pokercity.lobby.lobby",   # Ganti dengan activity utama aplikasi
        "udid": udid,
        "automationName": "UiAutomator2",
        "noReset": True                   # Tidak mengatur ulang data aplikasi
    }

    # Membuat koneksi ke Appium Server
    driver = webdriver.Remote(remote_url, desired_caps)
    driver.implicitly_wait(10)
    return driver

def proses_awal(driver):
    actions = ActionChains(driver)

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
    
    
def proses_dua(driver):
    actions = ActionChains(driver)
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


def worker(section, jumlah_klaim):
    driver = run_automation(section)
    try: 
        print(f"[{section}] Proses awal Berjalan. . .")
        proses_awal(driver)
        for i in range(jumlah_klaim):
            print(f"[{section}] Proses Klaim ke-{i + 1}. . .")
            proses_dua(driver)
            time.sleep(0.5)
        print(f"[{section}] Klaim Selesai.")
    except Exception as e:
        print(f"[{section}] Terjadi error: {e}")
    finally:
        driver.quit()

def main_proses():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    sections = config.sections()
    
    jumlah_klaim = 0
    while True:
            try :
                jumlah_klaim = int(input("Masukkan jumlah : "))
                if jumlah_klaim > 0:
                    break
                else:
                    print("ulangi !")
                    
            except ValueError :
                print("Salah blok, masukkan angka ")
    
    threads = []
    for section in sections:
        thread = threading.Thread(target=worker, args=(section, jumlah_klaim))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    main_proses()
