#Instalar sqlite3 de la pagina oficial: https://www.sqlite.org/download.html
#Instalar sqlitebrowser de la página oficial: https://sqlitebrowser.org/dl/
import sqlite3
import csv
import os
class cargaBBDD:
    def __init__(self) -> None:
        pass
    def cargar_BBDD_TuriStatSP(self):
        # Ruta del archivo CSV
        csv_file_path = os.path.join("persistencia/ficherosCSV", "DatosINE.csv")
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('persistencia/basesDeDatos/TuriStatSP-BBDD.db')
        cursor = conn.cursor()

        # Eliminar la tabla si existe
        cursor.execute('''DROP TABLE IF EXISTS TuristatSP_BBDD''')

        # Crear la tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS TuriStatSP_BBDD (
                            Total_Nacional TEXT,
                            Comunidades_Ciudades_Autonomas TEXT,
                            Provincias TEXT,
                            Residencia_del_viajero TEXT,
                            Periodo INTEGER,
                            Total INTEGER
                        )''')
        # Leer los datos del archivo CSV y cargarlos en la base de datos
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            next(csvreader)  # Saltar la primera fila si contiene encabezados

            for row in csvreader:
                Total_Nacional, Comunidades_Ciudades_Autonomas, Provincias, Residencia_del_viajero, Periodo, Total = row
                # Reemplazar '..' con None para manejar los valores faltantes
                if Total == '..':
                    Total = None
                else:
                    Total = int(Total.replace(".", "")) # Convertir el total a entero
                
                # Insertar fila en la base de datos
                cursor.execute('''INSERT INTO TuriStatSP_BBDD VALUES (?, ?, ?, ?, ?, ?)''', 
                            (Total_Nacional, Comunidades_Ciudades_Autonomas, Provincias, Residencia_del_viajero, Periodo, Total))
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        print("Los datos se han cargado correctamente en la base de datos SQLite 'TuriStatSP-BBDD'.")
