import sqlite3
import persistencia.obtenerDatosJson as obtenerDatosJson


class Ranking:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/basesDeDatos/TuriStatSP-BBDD.db')
        self.cursor = self.conn.cursor()
        
    def mostrar_comunidades_mas_visitadas(self):
        self.cursor.execute('SELECT Comunidades_Ciudades_Autonomas, SUM(COALESCE(Total, 0)) AS TotalTuristas FROM TuriStatSP_BBDD WHERE Comunidades_Ciudades_Autonomas != "" AND Residencia_del_viajero = "Total " AND Provincias == "" GROUP BY Comunidades_Ciudades_Autonomas ORDER BY TotalTuristas DESC LIMIT 5')
        resultado = self.cursor.fetchall()
        datos_procesados = self.procesar_resultados(resultado)
        if datos_procesados:
            print("¡Procesamiento de la lista de comunidades más visitadas realizada con éxito!")
        else:
            print("¡Procesamiento de la lista de comunidades más visitadas no realizada correctamente!")
        return datos_procesados
   
    def mostrar_comunidades_menos_visitadas(self):
        self.cursor.execute('SELECT Comunidades_Ciudades_Autonomas, SUM(COALESCE(Total, 0)) AS TotalTuristas FROM TuriStatSP_BBDD WHERE Comunidades_Ciudades_Autonomas != "" AND Residencia_del_viajero = "Total " AND Provincias == "" GROUP BY Comunidades_Ciudades_Autonomas ORDER BY TotalTuristas ASC LIMIT 5')
        resultado = self.cursor.fetchall()
        datos_procesados = self.procesar_resultados(resultado)
        if datos_procesados:
            print("¡Procesamiento de la lista de comunidades menos visitadas realizada con éxito!")
        else:
            print("¡Procesamiento de la lista de comunidades menos visitadas no realizada correctamente!")
        return datos_procesados
        
    def procesar_resultados(self, resultado):
        datos_procesados = []
        if resultado:
            for i in resultado:
                comunidad = obtenerDatosJson.quitar_numeros_inicio(i[0])  # Eliminar los números al inicio del nombre de la provincia
                comunidad = obtenerDatosJson.mapear_provincia(comunidad)
                datos_procesados.append(comunidad)
        return datos_procesados