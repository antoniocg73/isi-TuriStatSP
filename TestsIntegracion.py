#Instalar pytest: pip install pytest
#Ejecutar test: pytest .\TestsIntegracion.py
import unittest
import requests
from dominio.login import Login
from dominio.ranking import Ranking
from dominio.seleccion import Seleccion
from dominio.TendenciasTuristas import TendenciasGrafico
class TestsIntegracion(unittest.TestCase):
 
    def test_integracion_datos(self):
        # Simular el comportamiento de la aplicación sin la interfaz gráfica
        # Aquí vamos a llamar directamente a los métodos de los módulos de dominio y verificar su comportamiento
        login = Login()
        assert login.verificar_usuario('usuario', 'contrasena') == False
        login = Login()
        assert login.verificar_usuario('georgiAC', 'manzana3') == True


        ranking = Ranking()
        assert ranking.mostrar_comunidades_mas_visitadas() == ["Andalucia", "Cataluna", "Canarias", "Comunidad Valenciana", "Baleares"]
        assert ranking.mostrar_comunidades_menos_visitadas() == ["Melilla", "Ceuta", "La Rioja", "Navarra", "Extremadura"]

        seleccion = Seleccion()
        assert seleccion.mostrar_numero_turistas("01 Andalucía", "2022") == [("01 Andalucía", 28786000)]
        assert seleccion.mostrar_comunidades("2022", 100000, 2) == [("19 Melilla",), ("18 Ceuta",)]

        tendencias = TendenciasGrafico()
        assert tendencias.fetch_data("01 Andalucía", "2018", "2022") == [["01 Andalucía", 2018, 7793000, 13317000], ["01 Andalucía", 2019, 9347000, 15598000],
                                    ["01 Andalucía", 2020, 6231000, 4055000], ["01 Andalucía", 2021, 9435000, 6674000], ["01 Andalucía", 2022, 12375000, 16410000]]

class TestIntegracionAPI(unittest.TestCase):
    def test_get_data(self):
        """
        Test para verificar que la API responde correctamente a una petición GET.
        """
        url = 'http://127.0.0.1:5000/get_data'
        expected_data = [
            {
                "comunidad": "Andalucia",
                "latitud": 37.3399964,
                "longitud": -4.5811614,
                "total": 101237000
            },
            {
                "comunidad": "Aragon",
                "latitud": 41.3787291,
                "longitud": -0.7639373,
                "total": 5474000
            }
        ]

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Convertir la respuesta JSON en un objeto Python y compararlo con los datos esperados
        actual_data = response.json()
        actual_data_subset = actual_data[:2]  # Solo se comprueban las dos primeras entradas
        
        for actual, expected in zip(actual_data_subset, expected_data):
            self.assertEqual(actual['comunidad'], expected['comunidad'])
            self.assertAlmostEqual(actual['latitud'], expected['latitud'], places=7)
            self.assertAlmostEqual(actual['longitud'], expected['longitud'], places=7)
            self.assertEqual(actual['total'], expected['total'])

# Si este script se ejecuta directamente, correr las pruebas
if __name__ == '__main__':
    unittest.main()

