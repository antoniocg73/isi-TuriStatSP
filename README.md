# TuriStatSP
Repositorio del laboratorio de Integración de Sistemas de Información

El usuario debe descargarse flask_cors, flask, requests, beautifulsoup4, sqlite3, sqlitebrowser, matplotlib, numpy y pytest.

pip install matplotlib requests numpy beautifulsoup4 flask flask_cors pytest

Sqlite3 en: https://www.sqlite.org/download.html
Sqlitebrowser: https://sqlitebrowser.org/dl/

## Inicialización de la aplicación
Primero debe de estar el servidor Flask encendido, para que la aplicación funcione correctamente.
1. Nos metemos en la carpeta persistencia desde la terminal (y dependiendo de donde lo guardes). "cd isi-TuriStatSP/persistencia"
2. Desde la terminal, estamos situados en persistencia y tenemos que iniciar el servidor mediante “obtenerDatosJson.py”. Por lo que escribimos “export FLASK_APP=obtenerDatosJson” y luego “flask run”. 
3. Una vez tenemos esto, ejecutamos el “manager.py” que está en "isi-TuriStatSP"

## DATOS DE USUARIO PARA LOGIN 
También, la base de datos de los usuarios tiene 3 usuarios predefinidos, que son los siguientes:
-	antonioCG con contraseña “4567”
-	georgiAC con contraseña “manzana3”
-	noeliaDA con contraseña “patata2”
También se pueden añadir nuevos usuarios.

