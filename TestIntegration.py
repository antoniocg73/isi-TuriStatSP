#Instalar pytest: pip install pytest

import unittest
from unittest.mock import patch
from presentacion.InterfazAplicacion import InterfazAplicacion

class TestIntegration(unittest.TestCase):

    @patch('dominio.login.Login.registrar_usuario')
    @patch('dominio.login.Login.verificar_usuario')
    @patch('dominio.ranking.Ranking.mostrar_comunidades_mas_visitadas')
    @patch('dominio.ranking.Ranking.mostrar_comunidades_menos_visitadas')
    @patch('dominio.seleccion.Seleccion.mostrar_numero_turistas')
    @patch('dominio.seleccion.Seleccion.mostrar_comunidades')
    def test_integration(self, mock_mostrar_comunidades, mock_mostrar_numero_turistas,
                         mock_mostrar_comunidades_menos_visitadas, mock_mostrar_comunidades_mas_visitadas,
                         mock_verificar_usuario, mock_registrar_usuario):
        
        # Configuración de los mocks
        mock_registrar_usuario.return_value = True
        mock_verificar_usuario.return_value = True
        mock_mostrar_comunidades_mas_visitadas.return_value = ["Andalucía", "Cataluña"]
        mock_mostrar_comunidades_menos_visitadas.return_value = ["La Rioja", "Cantabria"]
        mock_mostrar_numero_turistas.return_value = [("Andalucía", 100000)]
        mock_mostrar_comunidades.return_value = [("Andalucía", 100000)]

        # Inicializar la interfaz de la aplicación
        app = InterfazAplicacion()

        # Realizar las pruebas de interacción, por ejemplo, haciendo clic en botones,
        # ingresando datos en campos, etc., y verificando que la interfaz responda correctamente
        # y que los métodos de las clases de dominio se llamen correctamente.

if __name__ == '__main__':
    unittest.main()
