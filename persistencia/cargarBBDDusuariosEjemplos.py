import sqlite3
class cargarBBDDusuariosEjemplos:
    def __init__(self):
        # Ejemplos de usuarios y contraseñas
        self.ejemplos = [
            ('antonioCG', '4567'),
            ('noeliaDA', 'patata2'),
            ('georgiAC', 'manzana3')
        ]
    def cargar_BBDD_usuarios_ejemplos(self):
        # Conectar a la base de datos o crearla si no existe
        conn = sqlite3.connect('persistencia/basesDeDatos/usuarios.db')
        cursor = conn.cursor()

        # Crear la tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                            Usuario TEXT PRIMARY KEY,
                            Contrasena TEXT NOT NULL
                        )''')

        # Insertar los ejemplos en la tabla
        try:
            cursor.executemany('INSERT INTO Usuarios (Usuario, Contrasena) VALUES (?, ?)', self.ejemplos)
            conn.commit()
            print("Los datos se han cargado correctamente en la base de datos SQLite 'usuarios.db'.")
        except sqlite3.IntegrityError:
            print("Error: Los usuarios y contraseñas ya existen en la base de datos.")

        # Cerrar la conexión
        conn.close()

    if __name__ == "__main__":
        cargar_BBDD_usuarios_ejemplos()
