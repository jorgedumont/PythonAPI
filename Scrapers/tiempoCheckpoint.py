import requests
from bs4 import BeautifulSoup
import pandas as pd
from sys import argv
import json

def cargarDatosPuebloCheckpoint(nombrepueblo):
    nombrepueblo = nombrepueblo.replace(" ", "-")
    url = 'https://www.tutiempo.net/' + nombrepueblo + '.html?datos=detallados'
    if url is None:
        return False
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    columnas = ["idMunicipio","HumedadyPresion","UV"]
    columnas2 = ["Fecha"]
    df = pd.DataFrame(columns=columnas)
    df2 = pd.DataFrame(columns=columnas2)
    todosdias = soup.find("div", {"class": "tiledias"})
    for dia in todosdias.find_all("td"):
        fecha = dia.find("span", {"class": "day"}).get_text()
        fila2 = {"Fecha": fecha}
        df2 = df2.append(fila2, ignore_index=True)
    detalle = soup.find("div", {"class": "datadias detallado"})
    for datos in detalle.find_all("td"):
        datos1 = datos.find_all("span", {"class": "hrd"})
        datosuv = datos.find("span", {"class": "c4"})
        if datosuv is None:
            datosuv=0
        else:
            datosuv= datosuv.get_text()
        humedad = datos1[0]
        humedad = humedad.get_text().replace("%","")
        presion = datos1[1]
        presion = presion.get_text().replace("hPa","")
        humedadypresion = humedad +"-"+presion
        nombrepueblo = nombrepueblo.replace("-", " ")
        fila2 = {"idMunicipio":nombrepueblo,"HumedadyPresion": humedadypresion, "UV": datosuv}
        df = df.append(fila2, ignore_index=True)
    dfcombinado = pd.concat([df, df2], axis=1)
    #print(dfcombinado)
    #print(dfcombinado)
    #header = ["idMunicipio","Nombre", "Fecha", "tMaxima", "tMinima", "tMedia", "Humedad", "Presion", "Viento"]
    print(dfcombinado.to_json(orient='records',lines=False, force_ascii=False))
    #dfcombinado.to_csv("C:\\xampp\\htdocs\\PC3\\PythonAPI"+"\\datatiempo.csv", index=False, encoding='utf-8-sig')

def comprobarPueblo(nombrepueblo):
    nombrespueblos = pd.read_excel("C:\\Users\\jdumo\\OneDrive\\Escritorio\\Proyecto2\\Datos\\list-mun-2012.xls")
    nombrespueblos["Municipio"] = nombrespueblos["Municipio"].str.lower()
    nombrespueblos = nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos

#print('¿Que localidad estas buscando?')
nombrepueblo = argv[1] 
#Hay que pasar el argv entrecomillado en la shell
#nombrepueblo = 'tres cantos'
if comprobarPueblo(nombrepueblo):
    cargarDatosPuebloCheckpoint(nombrepueblo)
else:
    print("Nombre del pueblo no correcto")

