import requests
from bs4 import BeautifulSoup as bs

# A continuación función que devuelve la temperatura máxima que hace en Beas de Segura en el día actual. Devuelve la palabra Error en caso de problemas de conexión
# Lo sacará de tutiempo.net/beas-de-segura.html, donde sacaremos las temperatura máxima.
# Esta WEB si le pasas a la URL la población, también la saca de otras, como por ejemplo tutiempo.net/almeria.html
# Con lo cual a esta función le pasaremos una población, con esta población compondrá la URL y, a esta, le haremos el WEB Scrapping para la temperatura máxima

def meteo (poblacion):

    # "https://www.tutiempo.net/beas-de-segura.html" esto es un ejemplo de URL

    url = "https://www.tutiempo.net/"+poblacion+".html"
    respuesta_WEB = requests.get(url)
    if respuesta_WEB.status_code != 200:
        return "Error"
    else:
        contenido_WEB = respuesta_WEB.content
        contenido_parseado = bs (contenido_WEB, 'html.parser')
        temp_max_raw = contenido_parseado.find_all ('span', attrs = {'class':'t max'})
        temp_max = temp_max_raw[0].text
        return temp_max






