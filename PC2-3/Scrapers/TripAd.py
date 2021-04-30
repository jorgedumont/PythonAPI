import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd


def tripAd(vArg):
    # Recogemos el parametro de entrada para realizar el Web Scraping
    # vArg = "soto del real"

    # Opciones de navegacion
    vOptions = webdriver.ChromeOptions()
    # vOptions.add_argument("--headless")

    # Path con el ejecutor del driver
    vDriverPath = "C:\\Users\\jdumo\\Downloads\\chromedriver.exe"
    vDriver = webdriver.Chrome(vDriverPath, chrome_options=vOptions)

    # Inciar en 2 pantalla
    vDriver.set_window_position(2000, 0)
    vDriver.maximize_window()
    time.sleep(1)

    # Inicializamos el navegador
    vDriver.get('https://www.tripadvisor.es/')

    # Cookies
    try:
        WebDriverWait(vDriver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.evidon-banner-acceptbutton'))).click()
    except:
        print("No hay cookies para aceptar")

    # Buscador Principal
    WebDriverWait(vDriver, 10) \
        .until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/div[2]/div[2]/form/input[1]'))).send_keys(vArg)

    WebDriverWait(vDriver, 5) \
        .until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/div[2]/div[2]/form/button[3]'))).click()

    vDriver.implicitly_wait(5)

    # Cookies 2 pagina
    try:
        WebDriverWait(vDriver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._evidon-accept-button'))).click()
    except:
        print("No hay coockies para aceptar")

    # Buscador de Geolocalizacion
    WebDriverWait(vDriver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="GEO_SCOPED_SEARCH_INPUT"]'))).click()

    WebDriverWait(vDriver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CLEAR_WHERE"]'))).click()

    WebDriverWait(vDriver, 10) \
        .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="GEO_SCOPED_SEARCH_INPUT"]'))).send_keys('España')

    WebDriverWait(vDriver, 5) \
        .until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="TYPEAHEAD_RESULTS_OVERLAY"]/div[1]/div/div[2]/div/div/ul/li[1]'))).click()

    # Filtro "Ubicaciones"
    time.sleep(3)
    vUbi = vDriver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[7]/a')
    vUbi.click()

    WebDriverWait(vDriver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[3]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div/div'))).click()

    # Para cambiar la nueva pestaña a la actual y recogerla para trabajar con BS
    vDriver.switch_to_window(vDriver.window_handles[-1])
    vUrlLocalidad = vDriver.current_url

    vPage = requests.get(vUrlLocalidad)
    vSoup = BeautifulSoup(vPage.content, 'html.parser')
    vUrl = 'https://www.tripadvisor.es'
    # print(vUrlLocalidad)
    # print(vUrl)

    vLocalidadTitulo = vSoup.find("span", {"class": "{geoClass}"})
    # print(vLocalidadTitulo.text)

    vCarruseles = vSoup.findAll("ul", {"class": "_5Vb6a0_6"}, limit=3)
    # Creacion de DataFrames
    dfOcio = pd.DataFrame(columns=['Municipio', 'Nombre', 'Comentario', 'Referencia'])
    dfHoteles = pd.DataFrame(
        columns=['Municipio', 'Nombre', 'Descripcion', 'Caracteristicas', 'Comentario', 'Referencia'])
    dfRestaurantes = pd.DataFrame(columns=['Municipio', 'Nombre', 'Detalles', 'Comentario', 'Referencia'])
    # Lista para almacenar todas las referencias tratadas en la funcion para su posterior uso en tripAdComentarios()
    lUrlComentarios = []

    for element in vCarruseles:
        vItem = element.findAll("li", {"class": "_1JJg_sXZ"})  # Cada item del crrusel
        for element1 in vItem:
            vElement1Url = element1.find('a')
            vElement1Url = vElement1Url['href']  # Preparamos la URL

            vElementTitulo = element1.find("div", {"class": "VQlgmkyI WullykOU _3WoyIIcL"})
            vCategoria = vElement1Url.split('_')[0]
            # Diferenciamos entre Ocio, Hoteles y Restaurantes
            if vCategoria == '/Attraction':
                vPage2 = requests.get(vUrl + vElement1Url)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vComentario1 = vSoup2.find("q", {"class": "IRsGHoPm"})
                # print('Titulo: '+vElementTitulo.text)
                # print('Comentario: '+vComentario1.text)
                # print('Referencia: '+vUrl+vElement1Url)
                # print('----------------------')
                dfOcio = dfOcio.append(
                    {'Municipio': vArg, 'Nombre': vElementTitulo.text, 'Comentario': vComentario1.text,
                     'Referencia': vUrl + vElement1Url}, ignore_index=True)
                lUrlComentarios.append(vUrl + vElement1Url)


            elif vCategoria == '/Hotel':
                # Lista para almacenar todas las caracteristicas de cada Hotel y exportarla al df
                lCaracteristicas = []

                vPage2 = requests.get(vUrl + vElement1Url)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vDescripcion = vSoup2.find("div", {"class": "cPQsENeY"})
                vComentario2 = vSoup2.find("q", {"class": "IRsGHoPm"})
                vCaracteristicas = vSoup2.findAll("div", {"class": "_2rdvbNSg"})
                for i in vCaracteristicas:
                    lCaracteristicas.append(i.text)

                lCaracteristicas = str(lCaracteristicas)
                lCaracteristicas = lCaracteristicas.replace("[", "")
                lCaracteristicas = lCaracteristicas.replace("]", "")

                if vDescripcion != None:
                    # print('Titulo: '+vElementTitulo.text)
                    # print('Descripcion: '+vDescripcion.text)
                    # print(lCaracteristicas)
                    # print('Comentario: '+vComentario2.text)
                    # print('Referencia: '+vUrl+vElement1Url)
                    # print('----------------------')
                    dfHoteles = dfHoteles.append(
                        {'Municipio': vArg, 'Nombre': vElementTitulo.text, 'Descripcion': vDescripcion.text,
                         'Caracteristicas': lCaracteristicas, 'Comentario': vComentario2.text,
                         'Referencia': vUrl + vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl + vElement1Url)
                else:
                    vDescripcion = 'No hay descripcion'
                    # print('Titulo: '+vElementTitulo.text)
                    # print('Descripcion: '+vDescripcion)
                    # print(lCaracteristicas)
                    # print('Comentario: '+vComentario2.text)
                    # print('Referencia: '+vUrl+vElement1Url)
                    # print('----------------------')
                    dfHoteles = dfHoteles.append(
                        {'Municipio': vArg, 'Nombre': vElementTitulo.text, 'Descripcion': vDescripcion.text,
                         'Caracteristicas': lCaracteristicas, 'Comentario': vComentario2.text,
                         'Referencia': vUrl + vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl + vElement1Url)


            else:
                vPage2 = requests.get(vUrl + vElement1Url)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vComentario3 = vSoup2.find("p", {"class": "partial_entry"})
                vDetalles = vSoup2.find("div", {"class": "_1XLfiSsv"})
                if vDetalles != None:
                    # print('Titulo: '+vElementTitulo.text)
                    # print('Detalles: '+vDetalles.text)
                    # print('Comentario: '+vComentario3.text)
                    # print('Referencia: '+vUrl+vElement1Url)
                    # print('----------------------')
                    dfRestaurantes = dfRestaurantes.append(
                        {'Municipio': vArg, 'Nombre': vElementTitulo.text, 'Detalles': vDetalles.text,
                         'Comentario': vComentario3.text, 'Referencia': vUrl + vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl + vElement1Url)
                else:
                    vDetalles = 'Sin especificar'
                    # print('Titulo: '+vElementTitulo.text)
                    # print('Detalles: '+vDetalles)
                    # print('Comentario: '+vComentario3.text)
                    # print('Referencia: '+vUrl+vElement1Url)
                    # print('----------------------')
                    dfRestaurantes = dfRestaurantes.append(
                        {'Municipio': vArg, 'Nombre': vElementTitulo.text, 'Detalles': vDetalles,
                         'Comentario': vComentario3.text, 'Referencia': vUrl + vElement1Url}, ignore_index=True)
                    lUrlComentarios.append(vUrl + vElement1Url)

    # print(dfOcio)
    # print(dfHoteles)
    # print(dfRestaurantes)
    dfOcio.to_csv("./Datos/dataOcio"+ vArg +".csv", encoding='utf-8-sig', sep=';', index=False)
    dfHoteles.to_csv("./Datos/dataHoteles"+ vArg +".csv", encoding='utf-8-sig', sep=';', index=False)
    dfRestaurantes.to_csv("./Datos/dataRestaurantes"+ vArg +".csv", encoding='utf-8-sig', sep=';', index=False)
    # print(lUrlComentarios)
    return tripAdComentarios(lUrlComentarios=lUrlComentarios, vArg=vArg)


def tripAdComentarios(lUrlComentarios, vArg):
    vUrl = 'https://www.tripadvisor.es'
    # Creacion del DataFrame
    dfComentarios = pd.DataFrame(columns=['Municipio', 'Nombre', 'Comentario', 'Referencia'])
    # Recorremos la lista recibida por parametro con las Url con las que se ha trabajado
    for i in lUrlComentarios:
        vPage = requests.get(i)
        vSoup = BeautifulSoup(vPage.content, 'html.parser')
        vTitulo = vSoup.find("h1", {"id": "HEADING"}) or vSoup.find("h1", {"class": "_3a1XQ88S"})
        # print('TITULO: '+vTitulo.text)

        vComentarios = vSoup.findAll("div", {"class": "Dq9MAugU T870kzTX LnVzGwUB"}) or vSoup.findAll("div", {
            "class": "_2wrUUKlw _3hFEdNs8"}) or vSoup.findAll("div", {"class": "review-container"})
        # Recorremos cada comentario para almacenarlo en el df
        for e in vComentarios:
            vC1 = e.find("q", {"class": "IRsGHoPm"}) or e.find("p", {"class": "partial_entry"})
            # print(vC1.text)
            # print('########################')
            dfComentarios = dfComentarios.append(
                {'Municipio': vArg, 'Nombre': vTitulo.text, 'Comentario': vC1.text, 'Referencia': i}, ignore_index=True)

        # Declaramos la paginacion y la recorremos en caso de que exista
        vPaginacion = vSoup.find("div", {"class": "pageNumbers"})
        if vPaginacion != None:
            vPaginacion = vPaginacion.findAll("a", {"class": "pageNum"})
            for n in vPaginacion:
                vUrlCompleta = vUrl + n['href']
                vPage2 = requests.get(vUrlCompleta)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vComentarios1 = vSoup2.findAll("div", {"class": "Dq9MAugU T870kzTX LnVzGwUB"}) or vSoup2.findAll("div",
                                                                                                                 {
                                                                                                                     "class": "_2wrUUKlw _3hFEdNs8"}) or vSoup2.findAll(
                    "div", {"class": "review-container"})
                for e1 in vComentarios1:
                    vC2 = e1.find("q", {"class": "IRsGHoPm"}) or e1.find("p", {"class": "partial_entry"})
                    # print(vC2.text)
                    # print('########################')
                    dfComentarios = dfComentarios.append(
                        {'Municipio': vArg, 'Nombre': vTitulo.text, 'Comentario': vC2.text, 'Referencia': vUrlCompleta},
                        ignore_index=True)
        else:
            print('No hay paginacion disponible')

        # print('--------------------------')

    # print(dfComentarios)
    dfComentarios.to_csv("./Datos/dataComentarios" + vArg +".csv", encoding='utf-8-sig', sep=';', index=False)

def comprobarPueblo(nombrepueblo):
    nombrespueblos=pd.read_excel("./Datos/list-mun-2012.xls")
    nombrespueblos["Municipio"]=nombrespueblos["Municipio"].str.lower()
    nombrespueblos=nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos

print('¿Que localidad estas buscando?')
vArg = input()
if comprobarPueblo(vArg):
    tripAd(vArg)
else:
    print("Nombre del pueblo no correcto")


