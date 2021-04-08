import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

vArg = "colmenar viejo"

#Opciones de navegacion
vOptions = webdriver.ChromeOptions()

vDriverPath = "C:\\Users\\jdumo\\Downloads\\chromedriver.exe"
vDriver = webdriver.Chrome(vDriverPath, options=vOptions)

#Inciar en 2 pantalla
vDriver.set_window_position(2000, 0)
vDriver.maximize_window()
time.sleep(1)

#Inicializamos el navegador
vDriver.get('https://www.airbnb.es/')

try:
    time.sleep(1)
    vCookies = vDriver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/section/footer/div[2]/button')
    vCookies.click()
except:
    print("No hay cookies para aceptar")

'''WebDriverWait(vDriver, 15)\
    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bigsearch-query-detached-query"]'))).send_keys(vArg)'''

time.sleep(2)
vBusq = vDriver.find_element_by_xpath('//*[@id="bigsearch-query-detached-query"]')
vBusq.send_keys(vArg)

WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._1mzhry13'))).click()

'''time.sleep(2)
vBusq = vDriver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[2]/button/div')
vBusq.click()
/html/body/div[6]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[5]/div[2]'''

vUrlCarrusel = vDriver.current_url
#print(vUrlCarrusel)

#PRIMERO
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[1]'))).click()

vDriver.switch_to_window(vDriver.window_handles[-1])
vUrlOpcion1 = vDriver.current_url
#TITULO XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')))

vDriver.implicitly_wait(5)
#DESCRIPCION XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[2]/div')))

vDriver.implicitly_wait(5)
#DETALLES XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')))

vDriver.implicitly_wait(5)
#CARACTERISTICAS XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)
#RATINGS XPATH
WebDriverWait(vDriver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)

vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
vTitulo = vTitulo.text
vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
vDescripcion = vDescripcion.text
vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
vCaracteristicas = str(vCaracteristicas.text).split(" ")
vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
vDetalles = vDetalles.text
vRating = vDriver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/div[2]/div[1]/div/section/h2/span[2]/div')

print('Titulo: '+vTitulo)
print('Descripcion: '+vDescripcion)
print('Detalles: '+vDetalles)
print('Huespedes: '+vCaracteristicas[0])
print('nDormitorios: '+vCaracteristicas[3])
if vCaracteristicas[7] == 'cama' or 'camas':
        print('nCamas: '+vCaracteristicas[6])
        print('nBaños: '+vCaracteristicas[9])
else:
        print('nBaños: '+vCaracteristicas[6])
#print('Referencia: '+vUrlOpcion1)
vDriver.close()
vDriver.switch_to.window(vDriver.window_handles[0])
#print(vDriver.current_url)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
#vDriver.quit()
#print("/html/body/div[6]/div/div/div/div[1]/main/div/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[1]")
#print("/html/body/div[6]/div/div/div/div[1]/main/div/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[2]")
vDriver.implicitly_wait(10)
#SEGUNDO
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[2]'))).click()

vDriver.switch_to_window(vDriver.window_handles[-1])
vUrlOpcion1 = vDriver.current_url
#TITULO XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')))

vDriver.implicitly_wait(5)
#DESCRIPCION XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[2]/div')))

vDriver.implicitly_wait(5)
#DETALLES XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')))

vDriver.implicitly_wait(5)
#CARACTERISTICAS XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)
#RATINGS XPATH
WebDriverWait(vDriver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)

vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
vTitulo = vTitulo.text
vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
vDescripcion = vDescripcion.text
vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
vCaracteristicas = str(vCaracteristicas.text).split(" ")
vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
vDetalles = vDetalles.text
vRating = vDriver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/div[2]/div[1]/div/section/h2/span[2]/div')

print('Titulo: '+vTitulo)
print('Descripcion: '+vDescripcion)
print('Detalles: '+vDetalles)
print('Huespedes: '+vCaracteristicas[0])
print('nDormitorios: '+vCaracteristicas[3])
if vCaracteristicas[7] == 'cama' or 'camas':
        print('nCamas: '+vCaracteristicas[6])
        print('nBaños: '+vCaracteristicas[9])
else:
        print('nBaños: '+vCaracteristicas[6])
vDriver.close()
vDriver.switch_to.window(vDriver.window_handles[0])
#print('Referencia: '+vUrlOpcion1)
print('-------------------------------------------------------------')
#TERCERO
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[3]'))).click()

vDriver.switch_to_window(vDriver.window_handles[-1])
vUrlOpcion1 = vDriver.current_url
#TITULO XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[2]/div')))

vDriver.implicitly_wait(5)
#DESCRIPCION XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[2]/div[3]')))

vDriver.implicitly_wait(5)
#DETALLES XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')))

vDriver.implicitly_wait(5)
#CARACTERISTICAS XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div[2]/div')))

vDriver.implicitly_wait(5)
#RATINGS XPATH
WebDriverWait(vDriver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)

vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
vTitulo = vTitulo.text
vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
vDescripcion = vDescripcion.text
vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
vCaracteristicas = str(vCaracteristicas.text).split(" ")
vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
vDetalles = vDetalles.text
vRating = vDriver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/div[2]/div[1]/div/section/h2/span[2]/div')

print('Titulo: '+vTitulo)
print('Descripcion: '+vDescripcion)
print('Detalles: '+vDetalles)
print('Huespedes: '+vCaracteristicas[0])
print('nDormitorios: '+vCaracteristicas[3])
if vCaracteristicas[7] == 'cama' or 'camas':
        print('nCamas: '+vCaracteristicas[6])
        print('nBaños: '+vCaracteristicas[9])
else:
        print('nBaños: '+vCaracteristicas[6])
#print('Referencia: '+vUrlOpcion1)
vDriver.close()
vDriver.switch_to.window(vDriver.window_handles[0])
print('-------------------------------------------------------------')
#CUARTO
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[4]'))).click()

vDriver.switch_to_window(vDriver.window_handles[-1])
vUrlOpcion1 = vDriver.current_url
#TITULO XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')))

vDriver.implicitly_wait(5)
#DESCRIPCION XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[4]')))

vDriver.implicitly_wait(5)
#DETALLES XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')))

vDriver.implicitly_wait(5)
#CARACTERISTICAS XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)
#RATINGS XPATH
WebDriverWait(vDriver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)

vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
vTitulo = vTitulo.text
vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
vDescripcion = vDescripcion.text
vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
vCaracteristicas = str(vCaracteristicas.text).split(" ")
vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
vDetalles = vDetalles.text
vRating = vDriver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/div[2]/div[1]/div/section/h2/span[2]/div')

print('Titulo: '+vTitulo)
print('Descripcion: '+vDescripcion)
print('Detalles: '+vDetalles)
print('Huespedes: '+vCaracteristicas[0])
print('nDormitorios: '+vCaracteristicas[3])
if vCaracteristicas[7] == 'cama' or 'camas':
        print('nCamas: '+vCaracteristicas[6])
        print('nBaños: '+vCaracteristicas[9])
else:
        print('nBaños: '+vCaracteristicas[6])
#print('Referencia: '+vUrlOpcion1)
vDriver.close()
vDriver.switch_to.window(vDriver.window_handles[0])
print('-------------------------------------------------------------')
#QUINTO
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[4]'))).click()

vDriver.switch_to_window(vDriver.window_handles[-1])
vUrlOpcion1 = vDriver.current_url
#TITULO XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')))

vDriver.implicitly_wait(5)
#DESCRIPCION XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ExploreLayoutController"]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div[3]/div/div/div/div/div[5]')))

vDriver.implicitly_wait(5)
#DETALLES XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')))

vDriver.implicitly_wait(5)
#CARACTERISTICAS XPATH
WebDriverWait(vDriver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)
#RATINGS XPATH
WebDriverWait(vDriver, 15)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

vDriver.implicitly_wait(5)

vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
vTitulo = vTitulo.text
vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
vDescripcion = vDescripcion.text
vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
vCaracteristicas = str(vCaracteristicas.text).split(" ")
vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
vDetalles = vDetalles.text
vRating = vDriver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/div[2]/div[1]/div/section/h2/span[2]/div')

print('Titulo: '+vTitulo)
print('Descripcion: '+vDescripcion)
print('Detalles: '+vDetalles)
print('Huespedes: '+vCaracteristicas[0])
print('nDormitorios: '+vCaracteristicas[3])
if vCaracteristicas[7] == 'cama' or 'camas':
        print('nCamas: '+vCaracteristicas[6])
        print('nBaños: '+vCaracteristicas[9])
else:
        print('nBaños: '+vCaracteristicas[6])
#print('Referencia: '+vUrlOpcion1)
vDriver.close()
vDriver.switch_to.window(vDriver.window_handles[0])
print('-------------------------------------------------------------')