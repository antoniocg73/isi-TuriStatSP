#Instalar pytest: pip install pytest
#Ejecutar test: pytest .\TestIntegration.py
import unittest
from unittest.mock import patch, MagicMock
from presentacion.InterfazAplicacion import InterfazAplicacion
from dominio.login import Login
from dominio.ranking import Ranking
from dominio.seleccion import Seleccion

class TestIntegration(unittest.TestCase):
    '''
    @patch.object(Login, 'registrar_usuario')
    @patch.object(Login, 'verificar_usuario')
    @patch.object(Ranking, 'mostrar_comunidades_mas_visitadas')
    @patch.object(Ranking, 'mostrar_comunidades_menos_visitadas')
    @patch.object(Seleccion, 'mostrar_numero_turistas')
    @patch.object(Seleccion, 'mostrar_comunidades')
    '''
    def test_integration(self):
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

if __name__ == '__main__':
    unittest.main()
