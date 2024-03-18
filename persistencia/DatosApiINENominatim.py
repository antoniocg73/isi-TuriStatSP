import requests
import csv
import os

def obtener_latitudes_longitudes(comunidades, archivo_destino):
    url_base = 'https://nominatim.openstreetmap.org/search'
    
    with open(archivo_destino, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Comunidad', 'Latitud', 'Longitud'])

        for comunidad in comunidades:
            query = comunidad + ', Spain'
            parametros = {
                'q': query,
                'format': 'json'
            }
            respuesta = requests.get(url_base, params=parametros)
            data = respuesta.json()
            
            if data:
                latitud = data[0]['lat']
                longitud = data[0]['lon']
                csvwriter.writerow([comunidad, latitud, longitud])
            else:
                print(f"No se encontraron coordenadas para {comunidad}")

# Lista de comunidades autónomas y ciudades autónomas de España
comunidades = [
    'Andalucía', 'Aragón', 'Asturias', 'Baleares', 'Canarias', 'Cantabria', 'Castilla y León',
    'Castilla-La Mancha', 'Cataluña', 'Ceuta', 'Comunidad Valenciana', 'Extremadura', 'Galicia',
    'La Rioja', 'Madrid', 'Melilla', 'Murcia', 'Navarra', 'Euskadi'
]

# Directorio y nombre del archivo de destino
nombre_archivo_destino = 'persistencia/LatitudesLongitudes.csv'

# Obtener latitudes y longitudes y guardar en un archivo CSV
obtener_latitudes_longitudes(comunidades, nombre_archivo_destino)

print("Proceso completado. Se han guardado las latitudes y longitudes en el archivo:", nombre_archivo_destino)
