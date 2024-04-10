from presentacion.InterfazAplicacion import InterfazAplicacion
from persistencia.cargarBBDDCoordenadas import cargarBBDDCoordenadas
from persistencia.cargarBBDDusuariosEjemplos import cargarBBDDusuariosEjemplos
from persistencia.DatosApiINE import DatosApiINE
from persistencia.DatosApiINENominatim import DatosApiINENominatim
from persistencia.cargaBBDD import cargaBBDD
import os
if __name__ == '__main__':

    archivo1_db = "persistencia/basesDeDatos/usuarios.db"
    archivo2_db = "persistencia/basesDeDatos/ComunidadesCoordenadas.db"
    archivo3_db = "persistencia/basesDeDatos/TuriStatSP-BBDD.db"
    archivo4_db = "persistencia/ficherosCSV/DatosINE.csv"
    archivo5_db = "persistencia/ficherosCSV/LatitudesLongitudes.csv"

    # Utiliza os.path.exists para comprobar si el archivo existe.
    def existe_archivo(archivo1_db, archivo2_db, archivo3_db, archivo4_db, archivo5_db):
        if os.path.exists(archivo1_db) and os.path.exists(archivo2_db) and os.path.exists(archivo3_db) and os.path.exists(archivo4_db) and os.path.exists(archivo5_db):
            return True
        else:
            return False
        
    if not (existe_archivo(archivo1_db, archivo2_db, archivo3_db, archivo4_db, archivo5_db)):
        DatosApiINE().descargar_archivo()
        DatosApiINENominatim().obtener_latitudes_longitudes()
        cargaBBDD().cargar_BBDD_TuriStatSP()
        cargarBBDDCoordenadas().cargar_BBDD_coordenadas_comunidades()
        cargarBBDDusuariosEjemplos().cargar_BBDD_usuarios_ejemplos()
    #Siempre se ejecutará la interfaz de la aplicación
    InterfazAplicacion()

    
        