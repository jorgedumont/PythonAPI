from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

vArg = "colmenar viejo"
#Opciones de navegacion
vOptions = webdriver.ChromeOptions()
#vOptions.add_argument("--headless")

#Path con el ejecutor del driver
vDriverPath = "C:\\Users\\manu1\\Downloads\\chromedriver.exe"
vDriver = webdriver.Chrome(vDriverPath, chrome_options=vOptions)

#Inciar en 2 pantalla
vDriver.set_window_position(2000, 0)
vDriver.maximize_window()
time.sleep(1)

#Inicializamos el navegador
vDriver.get('https://www.tripadvisor.es/')

#Cookies
try:   
    WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/button[1]'))).click()
except:
    print("No hay cookies para aceptar")

#Buscador Principal  
WebDriverWait(vDriver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]'))).click()

WebDriverWait(vDriver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]'))).send_keys(vArg)

WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[3]/div/div/div[2]/form/button[3]'))).click()

vDriver.implicitly_wait(5)

#Cookies 2 pagina
try:   
    WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._evidon-accept-button'))).click()
except:
    print("No hay coockies para aceptar")

#Buscador de Geolocalizacion
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="GEO_SCOPED_SEARCH_INPUT"]'))).click()

WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CLEAR_WHERE"]'))).click()

WebDriverWait(vDriver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="GEO_SCOPED_SEARCH_INPUT"]'))).send_keys('España')

WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="TYPEAHEAD_RESULTS_OVERLAY"]/div[1]/div/div[2]/div/div/ul/li[1]'))).click()

#Filtro "Ubicaciones"
time.sleep(3)
vUbi = vDriver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[7]/a')
vUbi.click()

WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div/div/div'))).click()

#Para cambiar la nueva pestaña a la actual y recogerla para trabajar con BS
vDriver.switch_to_window(vDriver.window_handles[-1])