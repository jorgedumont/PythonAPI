import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
def Airbnb(vArg):

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
        dfCasas = pd.DataFrame(columns=['Municipio', 'Titulo', 'Descripcion', 'Detalles', 'Caracteristicas'])
        time.sleep(2)
        vBusq = vDriver.find_element_by_xpath('//*[@id="bigsearch-query-detached-query"]')
        vBusq.send_keys(vArg)

        WebDriverWait(vDriver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._1mzhry13'))).click()

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

        vTitulo = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
        vTitulo = vTitulo.text
        vDescripcion = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
        vDescripcion = vDescripcion.text
        vCaracteristicas = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
        vCaracteristicas = str(vCaracteristicas.text)
        vDetalles = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
        vDetalles = vDetalles.text
        dfCasas = dfCasas.append(
                {'Municipio': vArg, 'Titulo':vTitulo, 'Descripcion':vDescripcion, 'Detalles':vDetalles, 'Caracteristicas':vCaracteristicas }, ignore_index=True)
        vDriver.close()
        vDriver.switch_to.window(vDriver.window_handles[0])
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

        vTitulo2 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
        vTitulo2 = vTitulo2.text
        vDescripcion2 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
        vDescripcion2 = vDescripcion2.text
        vCaracteristicas2 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
        vCaracteristicas2 = str(vCaracteristicas2.text)
        vDetalles2 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
        vDetalles2 = vDetalles2.text
        dfCasas = dfCasas.append(
                {'Municipio': vArg, 'Titulo': vTitulo2, 'Descripcion': vDescripcion2, 'Detalles': vDetalles2,
                 'Caracteristicas': vCaracteristicas2}, ignore_index=True)
        vDriver.close()
        vDriver.switch_to.window(vDriver.window_handles[0])
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
                .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-content"]/div/div/div[3]/div[1]/div/div[2]/div')))

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

        vTitulo3 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
        vTitulo3 = vTitulo3.text
        vDescripcion3 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
        vDescripcion3 = vDescripcion3.text
        vCaracteristicas3 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
        vCaracteristicas3 = str(vCaracteristicas3.text)
        vDetalles3 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
        vDetalles3 = vDetalles3.text
        dfCasas = dfCasas.append(
                {'Municipio': vArg, 'Titulo': vTitulo3, 'Descripcion': vDescripcion3, 'Detalles': vDetalles3,
                 'Caracteristicas': vCaracteristicas3}, ignore_index=True)
        vDriver.close()
        vDriver.switch_to.window(vDriver.window_handles[0])
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

        vTitulo4 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
        vTitulo4 = vTitulo4.text
        vDescripcion4 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
        vDescripcion4 = vDescripcion4.text
        vCaracteristicas4 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
        vCaracteristicas4 = str(vCaracteristicas4.text)
        vDetalles4 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
        vDetalles4 = vDetalles4.text
        dfCasas = dfCasas.append(
                {'Municipio': vArg, 'Titulo': vTitulo4, 'Descripcion': vDescripcion4, 'Detalles': vDetalles4,
                 'Caracteristicas': vCaracteristicas4}, ignore_index=True)
        vDriver.close()
        vDriver.switch_to.window(vDriver.window_handles[0])
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

        vTitulo5 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[1]/div[1]/div/div/div/div/section/div[1]/h1')
        vTitulo5 = vTitulo5.text
        vDescripcion5 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[3]/div/div[2]/div[1]/span/div')
        vDescripcion5 = vDescripcion5.text
        vCaracteristicas5 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[1]/div[2]')
        vCaracteristicas5 = str(vCaracteristicas5.text)
        vDetalles5 = vDriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/div/div[5]/div/div[2]/div/div[2]')
        vDetalles5 = vDetalles5.text
        dfCasas = dfCasas.append(
                {'Municipio': vArg, 'Titulo': vTitulo5, 'Descripcion': vDescripcion5, 'Detalles': vDetalles5,
                 'Caracteristicas': vCaracteristicas5}, ignore_index=True)
        vDriver.close()
        vDriver.switch_to.window(vDriver.window_handles[0])
        dfCasas.to_csv("./Datos/dataCasas" + vArg + ".csv", encoding='utf-8-sig', sep=';', index=False)

def comprobarPueblo(nombrepueblo):
    nombrespueblos=pd.read_excel("./Datos/list-mun-2012.xls")
    nombrespueblos["Municipio"]=nombrespueblos["Municipio"].str.lower()
    nombrespueblos=nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos


print('¿Que localidad estas buscando?')
vArg = input()
if comprobarPueblo(vArg):
    Airbnb(vArg)
else:
    print("Nombre del pueblo no correcto")
