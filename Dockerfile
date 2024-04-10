# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
RUN mkdir /appTuriStatSP

# Establece el directorio de trabajo en /app
WORKDIR /appTuriStatSP

# Copia el contenido del directorio actual al directorio de trabajo
ADD . /appTuriStatSP

# Copia el script obtenerDatosJson.py al directorio de trabajo
COPY persistencia/obtenerDatosJson.py .

# Copia las bases de datos A y B al directorio de trabajo
COPY persistencia/basesDeDatos/TuriStatSP-BBDD.db /appTuriStatSP/basesDeDatos/TuriStatSP-BBDD.db
COPY persistencia/basesDeDatos/ComunidadesCoordenadas.db /appTuriStatSP/basesDeDatos/ComunidadesCoordenadas.db

# Instalar las dependencias necesarias
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta el script obtenerDatosJson.py cuando se inicia el contenedor
CMD ["python", "/appTuriStatSP/obtenerDatosJson.py"]
