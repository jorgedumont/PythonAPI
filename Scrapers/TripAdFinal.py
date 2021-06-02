import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
from sys import argv
import json
from textblob import TextBlob


def tripAd(vArg):
    
    vOptions = webdriver.ChromeOptions()
    #vOptions.add_argument("--headless")

    #Path con el ejecutor del driver
    vDriverPath = "C:\\Users\\jdumo\\Downloads\\chromedriver.exe"
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
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[3]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div'))).click()

    #Para cambiar la nueva pestaña a la actual y recogerla para trabajar con BS
    vWindow = vDriver.window_handles[-1]
    vDriver.switch_to.window(vWindow)
    vUrlLocalidad = vDriver.current_url


    vPage = requests.get(vUrlLocalidad)
    vSoup = BeautifulSoup(vPage.content, 'html.parser')
    vUrl = 'https://www.tripadvisor.es'
    #print(vUrlLocalidad)
    #print(vUrl)

    vLocalidadTitulo = vSoup.find("span", {"class":"{geoClass}"})
    #print(vLocalidadTitulo.text)

    vCarruseles = vSoup.findAll("ul", limit=3)
    #Creacion de DataFrames
    dfOcio = pd.DataFrame(columns=['Municipio', 'Nombre', 'Referencia'])
    dfHoteles = pd.DataFrame(columns=['Municipio', 'Nombre', 'Descripcion', 'Caracteristicas', 'Referencia'])
    dfRestaurantes = pd.DataFrame(columns=['Municipio', 'Nombre', 'Detalles', 'Referencia'])
    #Lista para almacenar todas las referencias tratadas en la funcion para su posterior uso en tripAdComentarios()
    lUrlComentarios = []

    for element in vCarruseles:
        vItem = element.findAll("li") #Cada item del crrusel
        for element1 in vItem:
            vElement1Url = element1.find('a')
            vElement1Url = vElement1Url['href'] #Preparamos la URL
            
            vElementTitulo = element1.find("div", {"class":"VQlgmkyI WullykOU _3WoyIIcL"})
            vCategoria = vElement1Url.split('_')[0]
            #Diferenciamos entre Ocio, Hoteles y Restaurantes
            if vCategoria == '/Attraction':
                #print('Titulo: '+vElementTitulo.text)
                #print('Referencia: '+vUrl+vElement1Url)
                #print('----------------------')
                dfOcio = dfOcio.append({'Municipio':vArg, 'Nombre':vElementTitulo.text, 'Referencia':vUrl+vElement1Url}, ignore_index=True)
                lUrlComentarios.append(vUrl+vElement1Url)
                

            elif vCategoria == '/Hotel':
                #Lista para almacenar todas las caracteristicas de cada Hotel y exportarla al df
                lCaracteristicas = []

                vPage2 = requests.get(vUrl+vElement1Url)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vDescripcion = vSoup2.find("div", {"class":"cPQsENeY"})
                vCaracteristicas = vSoup2.findAll("div", {"class":"_2rdvbNSg"})
                for i in vCaracteristicas:
                    lCaracteristicas.append(i.text) 

                lCaracteristicas = str(lCaracteristicas)
                lCaracteristicas = lCaracteristicas.replace("[", "")
                lCaracteristicas = lCaracteristicas.replace("]", "")

                if vDescripcion != None:
                    #print('Titulo: '+vElementTitulo.text)
                    #print('Descripcion: '+vDescripcion.text)
                    #print(lCaracteristicas)             
                    #print('Referencia: '+vUrl+vElement1Url)
                    #print('----------------------')
                    dfHoteles = dfHoteles.append({'Municipio':vArg, 'Nombre':vElementTitulo.text, 'Descripcion':vDescripcion.text, 'Caracteristicas':lCaracteristicas, 'Referencia':vUrl+vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl+vElement1Url)
                else:
                    vDescripcion = 'No hay descripcion'
                    #print('Titulo: '+vElementTitulo.text)
                    #print('Descripcion: '+vDescripcion)
                    #print(lCaracteristicas)             
                    #print('Referencia: '+vUrl+vElement1Url)
                    #print('----------------------')
                    dfHoteles = dfHoteles.append({'Municipio':vArg, 'Nombre':vElementTitulo.text, 'Descripcion':vDescripcion.text, 'Caracteristicas':lCaracteristicas, 'Referencia':vUrl+vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl+vElement1Url)
            
                
            else:
                vPage2 = requests.get(vUrl+vElement1Url)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vDetalles = vSoup2.find("div", {"class":"_1XLfiSsv"})
                if vDetalles != None:
                    #print('Titulo: '+vElementTitulo.text)
                    #print('Detalles: '+vDetalles.text)
                    #print('Referencia: '+vUrl+vElement1Url)
                    #print('----------------------')
                    dfRestaurantes = dfRestaurantes.append({'Municipio':vArg, 'Nombre':vElementTitulo.text, 'Detalles':vDetalles.text, 'Referencia':vUrl+vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl+vElement1Url)
                else:
                    vDetalles = 'Sin especificar'
                    #print('Titulo: '+vElementTitulo.text)
                    #print('Detalles: '+vDetalles)
                    #print('Referencia: '+vUrl+vElement1Url)
                    #print('----------------------')
                    dfRestaurantes = dfRestaurantes.append({'Municipio':vArg, 'Nombre':vElementTitulo.text, 'Detalles':vDetalles, 'Referencia':vUrl+vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl+vElement1Url)
                    
    vOcioJSON = dfOcio.to_json(orient='records',lines=False)
    vHotelesJSON = dfHoteles.to_json(orient='records',lines=False)
    vRestaurantesJSON = dfRestaurantes.to_json(orient='records',lines=False)
    vLugaresJSON = {'ocio':json.loads(vOcioJSON), 'hoteles':json.loads(vHotelesJSON), 'restaurantes':json.loads(vRestaurantesJSON)}
    #print(vJSONF)
    return tripAdComentarios(lUrlComentarios=lUrlComentarios, vArg=vArg, vJSON=vLugaresJSON)


def tripAdComentarios(lUrlComentarios, vArg, vJSON):
    vUrl = 'https://www.tripadvisor.es'

    aSentimiento = []
    vContador = 0

    #Recorremos la lista recibida por parametro con las Url con las que se ha trabajado
    for i in lUrlComentarios:
        #print(i)
        vPage = requests.get(i)
        vSoup = BeautifulSoup(vPage.content, 'html.parser')
        vTitulo = vSoup.find("h1")#, {"id":"HEADING"}) or vSoup.find("h1", {"class":"_3a1XQ88S"})
        #print('TITULO: '+vTitulo.text)

        vFiltro = str(i).split("_")[0]
        #print(vFiltro)

        vComentarios = vSoup.findAll("div", {"class":"Dq9MAugU T870kzTX LnVzGwUB"}) or vSoup.findAll("div", {"class":"_2wrUUKlw _3hFEdNs8"}) or vSoup.findAll("div", {"class":"review-container"})
        #Recorremos cada comentario para almacenarlo en el df
        for e in vComentarios:
            vC1 = e.find("q") or e.find("p", {"class":"partial_entry"})
            try: 
                vAnalisis = TextBlob(vC1.text).translate(to='en')
            except:
                vAnalisis = TextBlob(vC1.text)
            vAnalisis1 = vAnalisis.polarity#).replace("Sentiment(polarity=","").replace(" subjectivity=","").replace(")","")
            aSentimiento.append(float(vAnalisis1))
            #print(vAnalisisF)
            #print("------------------------------------------")
            #print(vC1.text)
            #print('########################')
            #print(vContador)
            vContador+=1
    
    #print(aSentimiento)
    #print(vContador)
    vTotal = sum(aSentimiento)
    vTotalF = float("%.2f" % vTotal)
    #print(vTotal)
    #print(vTotalF)
    vAnalisisSentimientoFinal = vTotalF/vContador
    #print(vAnalisisSentimientoFinal)
    vJsonGlobal = {'lugares':vJSON, 'analisis sentimiento':vAnalisisSentimientoFinal}
    print(json.dumps(vJsonGlobal))
    

    


def comprobarPueblo(nombrepueblo):
    nombrespueblos=pd.read_excel("C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Datos\\list-mun-2012.xls")
    nombrespueblos["Municipio"]=nombrespueblos["Municipio"].str.lower()
    nombrespueblos=nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos

#print('¿Que localidad estas buscando?')
vArg = argv[1] #"colmenar viejo"
if comprobarPueblo(vArg):
    tripAd(vArg)
else:
    print("Nombre del pueblo no correcto")