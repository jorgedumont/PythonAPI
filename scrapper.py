import requests
from bs4 import BeautifulSoup
import pandas as pd


def cargarPueblo(nombrepueblo):
    nombrepueblo = nombrepueblo.replace(" ", "%20")
    url = 'https://www.eltiempo.es/buscar?q=' + nombrepueblo
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find("ul", {"class": "m_search_results"})
    link = links.find("a", href=True)
    return link['href']


# cargarPueblo()

def cargarPueblo2(nombrepueblo):
    url = cargarPueblo(nombrepueblo)
    if url is None:
        return False
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    columnas=["Fecha","Maxima","Minima","Temperatura 8:00","Temperatura 14:00","Temperatura 20:00","Media"]
    df=pd.DataFrame(columns=columnas)
    #nombrefichero = num1 + ".txt"
    #f = io.open(nombrefichero, 'w', encoding="utf-8")
    tabladias=soup.find("div",{"class":"m_table_weather_day_wrapper"})
    if tabladias != None:
        for dia in tabladias.find_all("div")[::11]:
            infofecha = dia.find("div", {"class": "m_table_weather_day_date"})
            #diasemana = infofecha.find("p", {"class": "m_table_weather_day_title"})
            fecha = infofecha.find("p", {"class": ""})
            maximaminima = dia.find("div", {"class": "m_table_weather_day_max_min"})
            maxima = maximaminima.find("span", {"class": "m_table_weather_day_max_temp"})
            minima = maximaminima.find("span", {"class": "m_table_weather_day_min_temp"})
            datostemp1 = dia.find_all("div", {"class": "m_table_weather_day_temp_wrapper"})
            temp1 = datostemp1[0].find("span")
            temp2 = datostemp1[1].find("span")
            temp3 = datostemp1[2].find("span")
            temp11 = int(maxima.get_text().replace("°", ""))
            temp22 = int(minima.get_text().replace("°", ""))
            tempmedia = int((temp11 + temp22))/2
            #f.writelines("Dia semana: " + diasemana.get_text().strip() + "\n")
            if  temp1:
                temp1= temp1.get_text().replace("°", "")
            if temp2:
                temp2=temp2.get_text().replace("°", "")
            if temp3:
                temp3=temp3.get_text().replace("°", "")
            fila={"Fecha":fecha.get_text().replace("\n", "").replace(" ", ""),"Maxima":temp11,"Minima":temp22,"Temperatura 8:00":temp1,"Temperatura 14:00":temp2,"Temperatura 20:00":temp3,"Media":tempmedia}
            df=df.append(fila,ignore_index=True)
        df.to_csv("./Datos/"+nombrepueblo+".csv",index=False)
        print(df)
    else:
        print("No funciona")

def comprobarPueblo(nombrepueblo):
    nombrespueblos=pd.read_excel("./Datos/list-mun-2012.xls")
    nombrespueblos["Municipio"]=nombrespueblos["Municipio"].str.lower()
    nombrespueblos=nombrespueblos["Municipio"].tolist()
    return nombrepueblo.lower() in nombrespueblos


nombrepueblo = 'tres cantos'
if comprobarPueblo(nombrepueblo):
    cargarPueblo2(nombrepueblo)
else:
    print("Nombre del pueblo no correcto")