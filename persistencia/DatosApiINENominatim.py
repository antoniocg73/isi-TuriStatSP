import requests
import csv
import os
class DatosApiINENominatim:
    def __init__(self):
        # Lista de comunidades autónomas y ciudades autónomas de España
        self.comunidades = [
    'Andalucía', 'Aragón', 'Asturias', 'Baleares', 'Canarias', 'Cantabria', 'Castilla y León',
    'Castilla-La Mancha', 'Cataluña', 'Ceuta', 'Comunidad Valenciana', 'Extremadura', 'Galicia',
    'La Rioja', 'Madrid', 'Melilla', 'Murcia', 'Navarra', 'Euskadi'
    ]
    # Directorio y nombre del archivo de destino
        self.nombre_archivo_destino = 'persistencia/ficherosCSV/LatitudesLongitudes.csv'
        self.url_base = 'https://nominatim.openstreetmap.org/search'
    def obtener_latitudes_longitudes(self):
        with open(self.nombre_archivo_destino, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Comunidad', 'Latitud', 'Longitud'])

            for comunidad in self.comunidades:
                query = comunidad + ', Spain'
                parametros = {
                    'q': query,
                    'format': 'json'
                }
                respuesta = requests.get(self.url_base, params=parametros)
                data = respuesta.json()
                
                if data:
                    latitud = data[0]['lat']
                    longitud = data[0]['lon']
                    csvwriter.writerow([comunidad, latitud, longitud])
                else:
                    print(f"No se encontraron coordenadas para {comunidad}")
            print("Proceso completado. Se han guardado las latitudes y longitudes en el archivo:", self.nombre_archivo_destino)

