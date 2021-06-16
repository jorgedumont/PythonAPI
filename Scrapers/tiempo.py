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
    columnas = ["idMunicipio"]
    columnas2 = ["UV","Descripcion", "Minutos_Piel_Clara", "Minutos_Piel_Oscura", "Factor_Proteccion_Piel_Clara", "Factor_Proteccion_Piel_Oscura"]
    df = pd.DataFrame(columns=columnas)
    df2 = pd.DataFrame(columns=columnas2)
    todosdias = soup.find("div", {"class": "tiledias"})
    for dia in todosdias.find_all("td"):
        fecha = dia.find("span", {"class": "day"})
        fecha = fecha.get_text()
        nombrepueblo = nombrepueblo.replace("-", " ")
        fila = {"idMunicipio":nombrepueblo}
        df = df.append(fila, ignore_index=True)
    uv = soup.find("table", {"class": "tablagenerica"})
    datosblabla = uv.find_all("tr")[2:]
    for datos in datosblabla:
        datos1 = datos.find_all("td")
        UV = datos1[0]
        UV = UV.get_text()
        descripcion = datos1[1]
        descripcion = descripcion.get_text()
        exposicionpielclara = datos1[2]
        exposicionpielclara = exposicionpielclara.get_text()
        exposicionpieloscura = datos1[3]
        exposicionpieloscura = exposicionpieloscura.get_text()
        factorpielclara = datos1[4]
        factorpielclara = factorpielclara.get_text()
        factorpieloscura = datos1[5]
        factorpieloscura = factorpieloscura.get_text()
        fila2 = {"UV": UV,"Descripcion": descripcion, "Minutos_Piel_Clara": exposicionpielclara, 
        "Minutos_Piel_Oscura" : exposicionpieloscura, "Factor_Proteccion_Piel_Clara": factorpielclara, 
        "Factor_Proteccion_Piel_Oscura": factorpieloscura}
        df2 = df2.append(fila2, ignore_index=True)
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
#nombrepueblo = argv[1]
 #Hay que pasar el argv entrecomillado en la shell
nombrepueblo = 'tres cantos'
if comprobarPueblo(nombrepueblo):
    cargarPueblo2(nombrepueblo)
else:
    print("Nombre del pueblo no correcto")

