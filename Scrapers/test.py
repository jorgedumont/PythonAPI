from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json


vData = [
    {
        Municipio: "tres cantos",
        Nombre: "VP Jardín de Tres Cantos Hotel",
        Comentario: "Soy recepcionista. La chica de la recepción me ha mentido diciendo que no había habitaciones esta noche. O bien han cerrado ventas mal o no han querido. Cualquiera diría que el turismo no esta en crisis con semejante personal que tan poco cuida a los clientes, que a día de hoy, tanta falta hacen en el sector turístico. Nada bueno que comentar. Nunca volveré a consultar disponibilidad en este hotel.",
        Referencia: "https://www.tripadvisor.es/Hotel_Review-g562662-d234295-Reviews-VP_Jardin_de_Tres_Cantos-Tres_Cantos.html"
    },
    {
        Municipio: "tres cantos",
        Nombre: "VP Jardín de Tres Cantos Hotel",
        Comentario: "grandes profesionales. la atención al cliente es excepcional. La limpieza chapeau. Javier y Mercedes son grandes profesionales y excelentes personas. Me hacen sentir como en casa. Respecto a la relación calidad-precio, no hay hotel que le pueda superar. El transporte público está muy cerca.",
        Referencia: "https://www.tripadvisor.es/Hotel_Review-g562662-d234295-Reviews-VP_Jardin_de_Tres_Cantos-Tres_Cantos.html"
    }
]
