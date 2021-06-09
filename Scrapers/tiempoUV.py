import requests
from bs4 import BeautifulSoup
import pandas as pd
from sys import argv
import json

def cargarPueblo2(nombrepueblo):
    nombrepueblo = nombrepueblo.replace(" ", "-")
    url = 'https://www.tutiempo.net/' + nombrepueblo + '.html?datos=detallados'
    if url is None:
        return False
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #columnas = ["idMunicipio","Nombre", "Fecha", "tMaxima", "tMinima", "tMedia"]
    columnas = ["idMunicipio","Nombre", "Fecha"]
    #columnas2 = ["Humedad", "Presion", "Viento"]
    columnas3 = ["UV","Todos los datos"]
    
    df = pd.DataFrame(columns=columnas)
    #df2 = pd.DataFrame(columns=columnas2)
    df3 = pd.DataFrame(columns=columnas3)
    todosdias = soup.find("div", {"class": "tiledias"})
    for dia in todosdias.find_all("td"):
        diasemana = dia.find("h3")
        fecha = dia.find("span", {"class": "day"}).get_text()
        maxima = dia.find("span", {"class": "t max"})
        minima = dia.find("span", {"class": "t min"})
        temp11 = int(maxima.get_text().replace("°", ""))
        temp22 = int(minima.get_text().replace("°", ""))
        tempmedia = int((temp11 + temp22)) / 2
        nombrepueblo = nombrepueblo.replace("-", " ")
        fila = {"idMunicipio":nombrepueblo,"Nombre": diasemana.get_text(), "Fecha": fecha}
        df = df.append(fila, ignore_index=True)
    detalle = soup.find("div", {"class": "datadias detallado"})
    for datos in detalle.find_all("td"):
        datos1 = datos.find_all("span", {"class": "hrd"})
        humedad = datos1[0]
        print(humedad)
        humedad = humedad.get_text().replace("%","")
        presion = datos1[1]
        presion = presion.get_text().replace("hPa","")
        viento = datos1[2]
        viento = viento.get_text().replace("km/h","")
        fila2 = {"Humedad": humedad, "Presion": presion, "Viento": viento}
        #df2 = df2.append(fila2, ignore_index=True)
        
        uv = datos1[3].get_text()
        fila3 = {"UV": uv,"Todos los datos":  "Humedad "  + humedad + " " +"Presion "  + presion + " "  + "Viento "  + viento  +"UV "  + uv }
        df3 = df3.append(fila3, ignore_index=True)
        
      
    
    
    
    
    dfcombinado = pd.concat([df, df3], axis=1)
    #print(dfcombinado)
    #print(dfcombinado)
    #header = ["idMunicipio","Nombre", "Fecha", "tMaxima", "tMinima", "tMedia", "Humedad", "Presion", "Viento"]
    print(dfcombinado.to_json(orient='records',lines=False, force_ascii=False))
    #dfcombinado.to_csv("C:\\xampp\\htdocs\\PC3\\PythonAPI"+"\\datatiempo.csv", index=False, encoding='utf-8-sig')

def comprobarPueblo(nombrepueblo):
    nombrespueblos = pd.read_excel("C:\\xampp\\htdocs\\PC3\\PythonAPI\\Datos\\list-mun-2012.xls")
    nombrespueblos["Municipio"] = nombrespueblos["Municipio"].str.lower()
    nombrespueblos = nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos

#print('¿Que localidad estas buscando?')
nombrepueblo = argv[1]
#nombrepueblo = 'tres cantos'
if comprobarPueblo(nombrepueblo):
    cargarPueblo2(nombrepueblo)
else:
    print("Nombre del pueblo no correcto")

