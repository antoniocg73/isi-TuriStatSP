# pip install requests (Consultas)
# pip install requests beautifulsoup4 (Web scrapping)
# Prototipo para el API de datos del INE
import requests
from bs4 import BeautifulSoup

# Descargar los datos en formato CSV
def descargar_archivo(url, nombre_archivo_destino):
    respuesta = requests.get(url)
    
    with open(nombre_archivo_destino, 'wb') as archivo:
        archivo.write(respuesta.content)

url = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48440.csv'

nombre_archivo_destino = 'persistencia/ficherosCSV/DatosINE.csv'

descargar_archivo(url, nombre_archivo_destino)


