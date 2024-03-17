from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    try:
        conn = sqlite3.connect('persistencia/TuriStatSP-BBDD.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Total_Nacional, Comunidades_Ciudades_Autonomas, Provincias, Residencia_del_viajero, Total FROM TuriStatSP_BBDD')
        data = cursor.fetchall()
        conn.close()

        # Formatear los datos en formato JSON
        formatted_data = []
        for row in data:
            formatted_data.append({
                'total_nacional': row[0],
                'comunidad': row[1],
                'provincia': row[2],
                'residencia_del_viajero': row[3],
                'total': row[4]
            })

        return jsonify(formatted_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
