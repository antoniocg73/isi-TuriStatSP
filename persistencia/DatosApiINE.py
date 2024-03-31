# pip install requests (Consultas)
# pip install beautifulsoup4 (Web scrapping)
# Prototipo para el API de datos del INE
import requests
from bs4 import BeautifulSoup
class DatosApiINE:
    def __init__(self):
        self.url = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48440.csv'
        self.nombre_archivo_destino = 'persistencia/ficherosCSV/DatosINE.csv'
    # Descargar los datos en formato CSV
    def descargar_archivo(self):
        respuesta = requests.get(self.url)
        
        with open(self.nombre_archivo_destino, 'wb') as archivo:
            archivo.write(respuesta.content)



