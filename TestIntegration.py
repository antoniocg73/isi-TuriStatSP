#Instalar pytest: pip install pytest
#Ejecutar test: pytest .\TestIntegration.py
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

        # Realizar las pruebas de interacción
        self.test_load_data_into_table(app, mock_mostrar_comunidades)
        self.test_select_item_from_list(app, mock_mostrar_numero_turistas)
        self.test_submit_form(app, mock_verificar_usuario)
        
    def test_load_data_into_table(self, app, mock_mostrar_comunidades):
        # Simula la carga de datos en una tabla de la interfaz
        app.load_data_into_table()

        # Verifica que se llame al método correspondiente en la clase de dominio
        mock_mostrar_comunidades.assert_called_once_with()  # Por ejemplo, carga de comunidades en una tabla

    def test_select_item_from_list(self, app, mock_mostrar_numero_turistas):
        # Simula la selección de un elemento de una lista en la interfaz
        app.select_item_from_list("Andalucía")  # Por ejemplo, selecciona la comunidad "Andalucía"

        # Verifica que se llame al método correspondiente en la clase de dominio
        mock_mostrar_numero_turistas.assert_called_once_with("Andalucía")  # Verifica que se pida el número de turistas para Andalucía

    def test_submit_form(self, app, mock_verificar_usuario):
        # Simula el ingreso de datos en un formulario de la interfaz
        app.fill_form_data("usuario", "contraseña")  # Por ejemplo, ingresa un usuario y contraseña en un formulario

        # Verifica que se llame al método correspondiente en la clase de dominio
        mock_verificar_usuario.assert_called_once_with("usuario", "contraseña")  # Verifica que se intente verificar el usuario con los datos ingresados

    def test_handle_button_click(self, app, mock_obtener_informacion_adicional):
        # Simula el clic en un botón de la interfaz
        app.handle_button_click()  # Por ejemplo, clic en un botón para mostrar información adicional

        # Verifica que se llame al método correspondiente en la clase de dominio
        mock_obtener_informacion_adicional.assert_called_once()  # Verifica que se solicite la información adicional al hacer clic en el botón

if __name__ == '__main__':
    unittest.main()
