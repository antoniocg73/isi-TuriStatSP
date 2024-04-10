#Instalar flask_cors con pip install flask_cors
#Instalar flask con pip install flask
from flask import Flask, jsonify, request
import sqlite3
import re 
from flask_cors import CORS  # Importa el módulo Flask-CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS en tu aplicación Flask

# Función para eliminar los números al inicio de una cadena
def quitar_numeros_inicio(cadena):
    return re.sub('^\d+\s*', '', cadena)

def mapear_provincia(nombre_provincia):
    mapeo = {
        'Andaluc\u00eda': 'Andalucia',
        'Arag\u00f3n': 'Aragon',
        'Asturias, Principado de': 'Asturias',
        'Balears, Illes': 'Baleares',
        'Canarias': 'Canarias',
        'Cantabria': 'Cantabria',
        'Castilla y Le\u00f3n': 'Castilla y Leon',
        'Castilla - La Mancha': 'Castilla-La Mancha',
        'Catalu\u00f1a': 'Cataluna',
        'Ceuta': 'Ceuta',
        'Comunitat Valenciana': 'Comunidad Valenciana',
        'Extremadura': 'Extremadura',
        'Galicia': 'Galicia',
        'Rioja, La': 'La Rioja',
        'Madrid, Comunidad de': 'Madrid',
        'Melilla': 'Melilla',
        'Murcia, Regi\u00f3n de': 'Murcia',
        'Navarra, Comunidad Foral de': 'Navarra',
        'Pa\u00eds Vasco': 'Pais Vasco'
    }
    return mapeo.get(nombre_provincia, nombre_provincia)  # Si el nombre de la provincia no está en el mapeo, se devuelve tal cual


@app.route('/get_data')
def get_data():
    conn = sqlite3.connect('basesDeDatos/TuriStatSP-BBDD.db')
    cursor = conn.cursor()
    #cursor.execute('SELECT Comunidades_Ciudades_Autonomas, Periodo, Residencia_del_viajero, COALESCE(Total, 0) FROM TuriStatSP_BBDD WHERE Comunidades_Ciudades_Autonomas != "" AND Residencia_del_viajero LIKE "Total " AND Provincias == "" ;')
    cursor.execute('SELECT Comunidades_Ciudades_Autonomas, SUM(COALESCE(Total, 0)) FROM TuriStatSP_BBDD WHERE Comunidades_Ciudades_Autonomas != "" AND Residencia_del_viajero = "Total " AND Provincias == "" GROUP BY Comunidades_Ciudades_Autonomas;')

    data = cursor.fetchall()
    conn.close()

    conn_coordenadas = sqlite3.connect('basesDeDatos/ComunidadesCoordenadas.db')
    cursor_coordenadas = conn_coordenadas.cursor()
    cursor_coordenadas.execute('SELECT Comunidad, Latitud, Longitud FROM CoordenadasComunidades')

    coordenadas = cursor_coordenadas.fetchall()
    conn_coordenadas.close()

    # Formatear los datos en formato JSON
    formatted_data = []

    for row in data:
        comunidad = quitar_numeros_inicio(row[0])  # Eliminar los números al inicio del nombre de la provincia
        comunidad = mapear_provincia(comunidad)
        total = row[1]

        # Buscar las coordenadas de la comunidad actual
        latitud = None
        longitud = None
        for coordenada in coordenadas:
            if comunidad.lower() == coordenada[0].lower():
                latitud = coordenada[1]
                longitud = coordenada[2]
                break

        formatted_data.append({
            'comunidad': comunidad,
            'total': total,
            'latitud': latitud,
            'longitud': longitud
        })

    return jsonify(formatted_data)


@app.route('/tendenciasComunidad')
def tendencias_comunidad():
    comunidad = request.args.get('comunidad', '12 Galicia')  # Por defecto se busca '12 Galicia'
    anio_inicio = request.args.get('anio_inicio', '2018')  # Año de inicio por defecto
    anio_fin = request.args.get('anio_fin', '2022')  # Año de fin por defecto
    
    conn = sqlite3.connect('basesDeDatos/TuriStatSP-BBDD.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            Comunidades_Ciudades_Autonomas,
            Periodo,
            SUM(CASE WHEN Residencia_del_viajero = 'Residentes en España' THEN Total ELSE 0 END) AS Residentes_Espana,
            SUM(CASE WHEN Residencia_del_viajero = 'Residentes en el Extranjero' THEN Total ELSE 0 END) AS Residentes_Extranjero
        FROM 
            TuriStatSP_BBDD
        WHERE 
            Comunidades_Ciudades_Autonomas = ?
            AND Provincias = ''
            AND Periodo BETWEEN ? AND ?
        GROUP BY 
            Comunidades_Ciudades_Autonomas,
            Periodo
        ORDER BY 
            Periodo
    ''', (comunidad, anio_inicio, anio_fin))
    
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)