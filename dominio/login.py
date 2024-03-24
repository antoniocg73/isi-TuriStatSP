import sqlite3

class Login:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/basesDeDatos/usuarios.db')
        self.cursor = self.conn.cursor()

    def verificar_usuario(self, usuario, contrasena):
        # Buscar en la base de datos si las credenciales son válidas
        self.cursor.execute('SELECT * FROM Usuarios WHERE Usuario=? AND Contrasena=?', (usuario, contrasena))
        resultado = self.cursor.fetchone()
        if resultado:
            print("¡Autenticación exitosa!")
            return True
        else:
            print("¡Autenticación fallida!")
            return False
        self.conn.close()
        