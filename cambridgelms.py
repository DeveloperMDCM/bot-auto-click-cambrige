from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#ciclos = 1000

path =  './driver/chromedriver.exe' # Ruta del driver
service = Service(executable_path=path)
web = 'https://www.cambridgelms.org/main/p/splash'

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=service, options=options)
# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
driver.get(web)

# Iniciar sesion
time.sleep(8)
 
username = driver.find_element(by='xpath', value='//*[@id="gigya-loginID-33136461830823732"]')
username.send_keys('tu usuario')
username = driver.find_element(by='xpath', value='//*[@id="gigya-password-272446220556026"]')
username.send_keys('tu clave')
login = driver.find_element(by='xpath', value='/html/body/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/form/div[2]/div[1]/div[4]/input')
driver.execute_script("arguments[0].click();", login)
time.sleep(7)  
continuar = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/section/div/form/div/a[2]')
driver.execute_script("arguments[0].click();", continuar)
time.sleep(2)  
curso = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/section/div/div/div/div/div/div/div/section/section/section/ul/li/div/a/span')
driver.execute_script("arguments[0].click();", curso)
time.sleep(2)  
unidad = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/section/div/div/section/section/div/form/div/ul/li[7]/a')
driver.execute_script("arguments[0].click();", unidad)
time.sleep(2)  
unidad = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/section/div/div/section/section/div/form/div/ul/li[7]/ul/li[2]/div/span')
driver.execute_script("arguments[0].click();", unidad)
time.sleep(2)  
unidad = driver.find_element(by='xpath', value='/html/body/div[2]/div/div/section/div/div/section/section/div/form/div/ul/li[7]/ul/li[2]/ul/li[2]/div/div[1]/a')
driver.execute_script("arguments[0].click();", unidad)


for i in range(ciclos):
        try:
            #si no se encuetra el elemento terminar_actividad click en siguiente
               
            print("Pulsando check")
            verificar = driver.find_element(by='xpath', value='/html/body/div[3]/div[3]/div/span[2]/a/span[2]')
        except:
            iniciando_unidad = driver.find_element(by='xpath', value='/html/body/div[2]/div[2]/div[2]/div/a') 
            print("Pasando a la suguiente...")
            driver.execute_script("arguments[0].click();", iniciando_unidad)
            pass
                
             
        


