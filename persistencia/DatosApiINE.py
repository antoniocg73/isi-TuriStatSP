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

nombre_archivo_destino = 'persistencia/DatosINE.csv'

descargar_archivo(url, nombre_archivo_destino)


# Obtener la última fecha de actualización de los datos
url = 'https://datos.gob.es/es/catalogo/ea0010587-datos-de-ocupacion-en-alojamientos-turisticos-y-otros-alojamientos-de-corta-estancia-anual-oat-identificador-api-48440'

respuesta = requests.get(url)

if respuesta.status_code == 200:

    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    elemento_fecha = soup.find('span', class_='automatic-local-datetime')
    
    if elemento_fecha and elemento_fecha.has_attr('data-datetime'):
        fecha_actualizacion = elemento_fecha['data-datetime']
        print('Fecha de última actualización (ISO 8601):', fecha_actualizacion)
    else:
        print('No se encontró la fecha de última actualización.')
else:
    print('Error al realizar la solicitud a la página:', respuesta.status_code)