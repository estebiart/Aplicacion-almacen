
import yaml
import argparse
import sqlite3


parser = argparse.ArgumentParser(description='--method GET, POST, PUT, DELETE . --servidor: IP o nombre del servidor donde se inicia la aplicación. Opcional. Por defecto localhost.--puerto: puerto donde se expondrá el API. Opcional. Por defecto 5000.--config: ruta y nombre del fichero de configuración de la aplicación. Obligatorio')

parser.add_argument("--servidor", type=str, default="localhost", required=False, help="Nombre o IP del servidor")
parser.add_argument( "--puerto", type=str, default='5000', required=False , help="Puerto para el servicio API")
parser.add_argument( "--config", type=str, required=True, help="Nombre y ruta del archivo de configuracion")

args = parser.parse_args()


def crearBD(dbBaseDatos):
    """Funcion crear base de datos"""  
    con = sqlite3.connect(dbBaseDatos)
    con.commit()
    con.close()

def crearTabla(dbBaseDatos):
    """Funcion crear tabla articulos"""
    con = sqlite3.connect(dbBaseDatos)
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE articulos (Id INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(50),unidades INTEGER, disponibilidad INTEGER)" )
        print("Tabla creada")       
    except sqlite3.OperationalError:
        print("La tabla articulos ya existe")    
    con.commit()
    con.close()

def insertarDato(dbBaseDatos,descripcion,cantidad,precio):
    """Funcion insertar articulos"""
    con = sqlite3.connect(dbBaseDatos)
    cur = con.cursor()
    try:      
        cur.execute("INSERT articulos VALUES"\
          "(?,?,?)",(descripcion,cantidad,precio) )
    except sqlite3.OperationalError:
        print("inserción exitosa")    
    con.commit()
    con.close()

def eliminarDato(dbBaseDatos,id):
    """Funcion eliminar articulo"""
    con = sqlite3.connect(dbBaseDatos)
    cur = con.cursor()
    try:      
       cur.execute('DELETE FROM articulos WHERE Id ="?"',(id) )
       for row in cur.execute('SELECT * FROM articulos'):
         print(row)
    except sqlite3.OperationalError:
        print("eliminacion exitosa")    
    con.commit()
    con.close()

def actualizarDato(dbBaseDatos,id):
    """Funcion actualizar articulos"""
    con = sqlite3.connect(dbBaseDatos)
    cur = con.cursor()
    try:      
        cur.execute('UPDATE articulos SET nombre="" WHERE Id ="?"',(id) )
        for row in cur.execute('SELECT * FROM articulos'):
         print(row)
    except sqlite3.OperationalError:
        print("eliminacion exitosa")    
    con.commit()
    con.close()

def leerRegistros(dbBaseDatos):
    """Funcion ver articulos"""
    con = sqlite3.connect(dbBaseDatos)
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM articulos'):
        print(row)
    con.close()   


if __name__ == "__main__":
    with open(args.config, 'r') as fileConfig:
        try:
            dicConfig = yaml.safe_load(fileConfig)
            dbBaseDatos = dicConfig["basedatos"]["path"]
        except yaml.YAMLError as exc:
            print(exc)
    fileConfig.close()        
    crearBD(dbBaseDatos)
    crearTabla(dbBaseDatos)
    leerRegistros(dbBaseDatos)
    descripcion = input('ingrese descripcion')
    cantidad = input('ingrese cantidad')
    precio = input('ingrese precio')
    insertarDato(dbBaseDatos,descripcion,cantidad,precio)
    id= input('ingrese id')
    actualizarDato(dbBaseDatos,id)
    id= input('ingrese id')
    eliminarDato(dbBaseDatos,id)







