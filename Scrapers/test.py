import json
import pandas as pd
from sys import argv
import json
import requests
from bs4 import BeautifulSoup

lURL = ['https://www.tripadvisor.es/Attraction_Review-g562662-d10021149-Reviews-Burrolandia-Tres_Cantos.html', 'https://www.tripadvisor.es/Attraction_Review-g562662-d4232311-Reviews-Castillo_de_Soto_de_Vinuelas-Tres_Cantos.html', 'https://www.tripadvisor.es/Attraction_Review-g562662-d8134852-Reviews-Parque_Central-Tres_Cantos.html', 
'https://www.tripadvisor.es/Attraction_Review-g562662-d4232303-Reviews-Casa_de_la_Cultura-Tres_Cantos.html', 'https://www.tripadvisor.es/Attraction_Review-g562662-d4232327-Reviews-Torre_del_Parque_Central-Tres_Cantos.html', 'https://www.tripadvisor.es/Attraction_Review-g562662-d12257045-Reviews-Noname_Sport-Tres_Cantos.html', 
'https://www.tripadvisor.es/Hotel_Review-g562662-d234295-Reviews-VP_Jardin_de_Tres_Cantos-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562662-d11737621-Reviews-Eurostars_Madrid_Foro-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562662-d229440-Reviews-Ramada_by_Wyndham_Madrid_Tres_Cantos-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562662-d319668-Reviews-Exe_Tres_Cantos-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562662-d20404555-Reviews-UrbanA_Tres_Cantos-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562662-d4437556-Reviews-Hostal_Tres_Cantos-Tres_Cantos.html', 'https://www.tripadvisor.es/Hotel_Review-g562660-d565272-Reviews-Globales_de_los_Reyes-San_Sebastian_de_los_Reyes.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d2724132-Reviews-Casa_Emeterio-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d2315133-Reviews-La_Terraza_De_Alba-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d8640014-Reviews-La_Bocatoma_Sabor_Venezolano-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d16211176-Reviews-Nawab_Indian_Cuisine-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d10457839-Reviews-Casa_Loren-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d4187836-Reviews-La_Churrasquita-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d4877525-Reviews-La_sarten_restaurante-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d4971947-Reviews-Pasteleria_Artesanal_Manolo-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d8779721-Reviews-Shoopo_HomeBar-Tres_Cantos.html', 'https://www.tripadvisor.es/Restaurant_Review-g562662-d4216769-Reviews-Mary_Carmen-Tres_Cantos.html']

vArg = "tres cantos"

def tripAdComentarios(lUrlComentarios, vArg):
    vUrl = 'https://www.tripadvisor.es'
    #Creacion del DataFrame
    dfComentariosOcio = pd.DataFrame(columns=['Municipio', 'Nombre', 'Comentario', 'Referencia'])
    dfComentariosHoteles = pd.DataFrame(columns=['Municipio', 'Nombre', 'Comentario', 'Referencia'])
    dfComentariosRestaurantes = pd.DataFrame(columns=['Municipio', 'Nombre', 'Comentario', 'Referencia'])
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
            vC1 = e.find("q", {"class":"IRsGHoPm"}) or e.find("p", {"class":"partial_entry"})
            #print(vC1.text)
            #print('########################')
            if "https://www.tripadvisor.es/Attraction" in vFiltro:
                dfComentariosOcio = dfComentariosOcio.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC1.text, 'Referencia':i}, ignore_index=True)
            elif "https://www.tripadvisor.es/Hotel" in vFiltro:
                dfComentariosHoteles = dfComentariosHoteles.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC1.text, 'Referencia':i}, ignore_index=True)
            else:
                dfComentariosRestaurantes = dfComentariosRestaurantes.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC1.text, 'Referencia':i}, ignore_index=True)
        
        #Declaramos la paginacion y la recorremos en caso de que exista    
        vPaginacion = vSoup.find("div", {"class":"pageNumbers"})
        if vPaginacion != None:
            vPaginacion = vPaginacion.findAll("a", {"class":"pageNum"})
            for n in vPaginacion:
                vUrlCompleta = vUrl+n['href']
                vPage2 = requests.get(vUrlCompleta)
                vSoup2 = BeautifulSoup(vPage2.content, 'html.parser')
                vComentarios1 = vSoup2.findAll("div", {"class":"Dq9MAugU T870kzTX LnVzGwUB"}) or vSoup2.findAll("div", {"class":"_2wrUUKlw _3hFEdNs8"}) or vSoup2.findAll("div", {"class":"review-container"})
                for e1 in vComentarios1:
                    vC2 = e1.find("q", {"class":"IRsGHoPm"}) or e1.find("p", {"class":"partial_entry"})
                    #print(vC2.text)
                    #print('########################')
                    if "https://www.tripadvisor.es/Attraction" in vFiltro:
                        dfComentariosOcio = dfComentariosOcio.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC2.text, 'Referencia':i}, ignore_index=True)
                    elif "https://www.tripadvisor.es/Hotel" in vFiltro:
                        dfComentariosHoteles = dfComentariosHoteles.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC2.text, 'Referencia':i}, ignore_index=True)
                    else:
                        dfComentariosRestaurantes = dfComentariosRestaurantes.append({'Municipio':vArg, 'Nombre':vTitulo.text, 'Comentario':vC2.text, 'Referencia':i}, ignore_index=True)
        
        else:
            print('No hay paginacion disponible')
                
        
        #print('--------------------------')
    
    vJSONOcio = dfComentariosOcio.to_json(orient='records', lines=False)
    vJSONHoteles= dfComentariosHoteles.to_json(orient='records', lines=False)
    vJSONRestaurantes = dfComentariosRestaurantes.to_json(orient='records', lines=False)
    vFinalJson = {'ocio':json.loads(vJSONOcio), 'hoteles':json.loads(vJSONHoteles), 'restaurantes':json.loads(vJSONRestaurantes)}
    #print(vJSONOcio)
    print(vFinalJson) 
    
    #print(vJSONHoteles)
    #print(vJSONRestaurantes)

tripAdComentarios(lURL, vArg)
