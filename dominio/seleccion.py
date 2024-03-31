import sqlite3
import persistencia.obtenerDatosJson as obtenerDatosJson


class Seleccion:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/basesDeDatos/TuriStatSP-BBDD.db')
        self.cursor = self.conn.cursor()
        
    def mostrar_numero_turistas(self, comunidad, anio):
        self.cursor.execute('SELECT Comunidades_Ciudades_Autonomas, SUM(COALESCE(Total, 0)) AS TotalC FROM TuriStatSP_BBDD WHERE Residencia_del_viajero = "Total " AND Provincias = "" AND Comunidades_Ciudades_Autonomas = ? AND Periodo = ? GROUP BY Comunidades_Ciudades_Autonomas', (comunidad, anio))
        resultado = self.cursor.fetchall()
        if resultado:
            print("¡Obtención del número de turistas con éxito!")
        else:
            print("¡Obtención del número de turistas no realizado correctamente!")
        return resultado
    
    def mostrar_comunidades(self, anio, numero_turistas, mas_o_menos):
        operator = '>' if mas_o_menos == 1 else '<'
        
        query = f'''SELECT Comunidades_Ciudades_Autonomas
                    FROM TuriStatSP_BBDD
                    WHERE Provincias = ''
                    AND Residencia_del_viajero = 'Total '
                    AND Periodo = ?
                    AND Total {operator} ?'''
        
        self.cursor.execute(query, (anio, numero_turistas))
        resultado = self.cursor.fetchall()
        
        if resultado:
            print(f"¡Obtención de comunidades {'con más' if mas_o_menos == 1 else 'con menos'} de {numero_turistas} turistas con éxito!")
        else:
            print(f"¡No se encontraron comunidades {'con más' if mas_o_menos == 1 else 'con menos'} de {numero_turistas} turistas en {anio}!")
            
        return resultado