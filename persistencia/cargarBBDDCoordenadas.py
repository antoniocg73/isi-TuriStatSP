import sqlite3
import csv
import os
class cargarBBDDCoordenadas:
    def __init__(self):
        # Mapeo de nombres de comunidades
        self.nombres_comunidades = {
            'Andalucía': 'Andalucia',
            'Aragón': 'Aragon',
            'Asturias': 'Asturias',
            'Baleares': 'Baleares',
            'Canarias': 'Canarias',
            'Cantabria': 'Cantabria',
            'Castilla y León': 'Castilla y Leon',
            'Castilla-La Mancha': 'Castilla-La Mancha',
            'Cataluña': 'Cataluna',
            'Ceuta': 'Ceuta',
            'Comunidad Valenciana': 'Comunidad Valenciana',
            'Extremadura': 'Extremadura',
            'Galicia': 'Galicia',
            'La Rioja': 'La Rioja',
            'Madrid': 'Madrid',
            'Melilla': 'Melilla',
            'Murcia': 'Murcia',
            'Navarra': 'Navarra',
            'Euskadi': 'Pais Vasco'
        }
    def cargar_BBDD_coordenadas_comunidades(self):
    # Ruta del archivo CSV con las coordenadas de las comunidades autónomas y ciudades autónomas
        csv_file_path = os.path.join("persistencia/ficherosCSV", "LatitudesLongitudes.csv")

        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('persistencia/basesDeDatos/ComunidadesCoordenadas.db')
        cursor = conn.cursor()

        # Eliminar la tabla si existe
        cursor.execute('''DROP TABLE IF EXISTS CoordenadasComunidades''')

        # Crear la tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS CoordenadasComunidades (
                            Comunidad TEXT,
                            Latitud REAL,
                            Longitud REAL
                        )''')

        # Leer los datos del archivo CSV y cargarlos en la base de datos
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Saltar la primera fila si contiene encabezados

            for row in csvreader:
                comunidad, latitud, longitud = row
                comunidad = self.nombres_comunidades.get(comunidad, comunidad)
                cursor.execute('''INSERT INTO CoordenadasComunidades VALUES (?, ?, ?)''', (comunidad, latitud, longitud))

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        print("Los datos se han cargado correctamente en la base de datos SQLite 'ComunidadesCoordenadas'.")