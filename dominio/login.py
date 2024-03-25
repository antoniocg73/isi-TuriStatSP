import sqlite3

class Login:
    def __init__(self):
        self.conn = sqlite3.connect('persistencia/basesDeDatos/usuarios.db')
        self.cursor = self.conn.cursor()

    def verificar_usuario(self, usuario, contrasena):
        # Buscar en la base de datos si las credenciales son válidas
        self.cursor.execute('SELECT * FROM Usuarios WHERE Usuario=? AND Contrasena=?', (usuario, contrasena))
        resultado = self.cursor.fetchone() 
        self.conn.close()
        if resultado:
            return True
        else:
            return False
        
    def registrar_usuario(self, usuario, contrasena):
        try:
            # Insertar en la base de datos el nuevo usuario
            self.cursor.execute('INSERT INTO Usuarios (Usuario, Contrasena) VALUES (?, ?)', (usuario, contrasena))
            self.conn.commit()
            return True
        except Exception as e:
            return False
        finally:
            self.conn.close()
        