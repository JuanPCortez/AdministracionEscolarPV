import mysql.connector
from mysql.connector import Error
from datetime import date
import pymysql

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='290993_Diego',
            database='uamitos'
        )
        if conexion.is_connected():
            print('Conexión exitosa a la base de datos.')
            return conexion
    except Error as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None

def obtener_usuario(clave):
    conexion = pymysql.connect(host="localhost", user="root", password="290993_Diego", database="uamitos")
    cursor = conexion.cursor(pymysql.cursors.DictCursor)

    consulta = "SELECT * FROM usuario WHERE clave = %s"
    cursor.execute(consulta, (clave,))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return resultado

def insertar_usuario(clave, nombre, apellidoP, apellidoM, edad, curp, correo, contrasena, rol):
    conexion = crear_conexion()
    if not conexion:
        return False
    
    cursor = conexion.cursor()
    query = "INSERT INTO usuario (clave, nombre, apellidoP, apellidoM, edad, curp, correo, contrasena, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (clave, nombre, apellidoP, apellidoM, edad, curp, correo, contrasena, rol)
    try:
        cursor.execute(query, datos)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al insertar:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def buscar_usuario(clave):
    conexion = crear_conexion()
    if not conexion:
        return None

    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM usuario WHERE clave = %s"
    try:
        cursor.execute(query, (clave,))
        resultado = cursor.fetchone()
        return resultado
    except Exception as e:
        print("Error al buscar usuario:", e)
        return None
    finally:
        cursor.close()
        conexion.close()

def actualizar_usuario(clave, nombre, apellidoP, apellidoM, edad, curp, correo, rol):
    conexion = crear_conexion()
    if not conexion:
        return False
    
    cursor = conexion.cursor()
    query = """
        UPDATE usuario
        SET nombre = %s,
            apellidoP = %s,
            apellidoM = %s,
            edad = %s,
            curp = %s,
            correo = %s,
            rol = %s
        WHERE clave = %s
    """
    datos = (nombre, apellidoP, apellidoM, edad, curp, correo, rol, clave)
    try:
        cursor.execute(query, datos)
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al actualizar:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def eliminar_usuario(clave):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "DELETE FROM usuario WHERE clave = %s"
    try:
        cursor.execute(query, (clave,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar usuario:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def obtener_ultimo_id_materia():
    conexion = crear_conexion()
    if not conexion:
        return 0

    cursor = conexion.cursor()
    query = "SELECT clave FROM materia WHERE clave LIKE 'MAT%' ORDER BY clave DESC LIMIT 1"
    try:
        cursor.execute(query)
        fila = cursor.fetchone()
        if fila:
            clave = fila[0]
            numero = int(clave[3:])
            return numero
        return 0
    except Exception as e:
        print("Error al obtener último ID de materia:", e)
        return 0
    finally:
        cursor.close()
        conexion.close()

def insertar_materia(clave, nombre, grado):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "INSERT INTO materia (clave, nombre, grado) VALUES (%s, %s, %s)"
    datos = (clave, nombre, grado)
    try:
        cursor.execute(query, datos)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al insertar materia:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def buscar_materia(clave):
    conexion = crear_conexion()
    if not conexion:
        return None

    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM materia WHERE clave = %s"
    try:
        cursor.execute(query, (clave,))
        resultado = cursor.fetchone()
        return resultado
    except Exception as e:
        print("Error al buscar materia:", e)
        return None
    finally:
        cursor.close()
        conexion.close()

def actualizar_materia(clave, nombre, grado):
    conexion = crear_conexion()
    if not conexion:
        return False
    
    cursor = conexion.cursor()
    query = """
        UPDATE materia
        SET nombre = %s,
            grado = %s
        WHERE clave = %s
    """
    datos = (nombre, grado, clave)
    try:
        cursor.execute(query, datos)
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al actualizar materia:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def eliminar_materia(clave):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "DELETE FROM materia WHERE clave = %s"
    try:
        cursor.execute(query, (clave,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar materia:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def insertar_anuncio(titulo, descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "INSERT INTO anuncio (titulo, descripcion, fecha_publicacion) VALUES (%s, %s, %s)"
    datos = (titulo, descripcion, date.today())
    try:
        cursor.execute(query, datos)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al insertar anuncio:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def buscar_anuncio(id_anuncio):
    conexion = crear_conexion()
    if not conexion:
        return None

    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM anuncio WHERE id = %s"
    try:
        cursor.execute(query, (id_anuncio,))
        return cursor.fetchone()
    except Exception as e:
        print("Error al buscar anuncio:", e)
        return None
    finally:
        cursor.close()
        conexion.close()

def actualizar_anuncio(id_anuncio, titulo, descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = """
        UPDATE anuncio
        SET titulo = %s,
            descripcion = %s
        WHERE id = %s
    """
    try:
        cursor.execute(query, (titulo, descripcion, id_anuncio))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al actualizar anuncio:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def eliminar_anuncio(id_anuncio):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "DELETE FROM anuncio WHERE id = %s"
    try:
        cursor.execute(query, (id_anuncio,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar anuncio:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def obtener_anuncios_recientes(limit=3):
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor(dictionary=True)
    try:
        query = "SELECT id, titulo, descripcion, fecha_publicacion FROM anuncio ORDER BY fecha_publicacion DESC LIMIT %s"
        cursor.execute(query, (limit,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al obtener anuncios:", e)
        return []
    finally:
        cursor.close()
        conexion.close()

def asignar_materia_profesor(clave_profesor, clave_materia, grupo):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "INSERT INTO profesor_materia_grupo (clave_materia, clave_profesor, grupo) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (clave_materia, clave_profesor, grupo))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al asignar materia a profesor:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def obtener_usuarios_por_prefijo(prefijo):
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor(dictionary=True)
    try:
        query = """
            SELECT clave, nombre, apellidoP, apellidoM
            FROM usuario
            WHERE clave LIKE %s
        """
        cursor.execute(query, (f"{prefijo}%",))
        return cursor.fetchall()
    except Exception as e:
        print("Error al obtener usuarios:", e)
        return []
    finally:
        cursor.close()
        conexion.close()

def obtener_materias():
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor(dictionary=True)
    try:
        query = "SELECT clave, nombre, grado FROM materia"
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al obtener materias:", e)
        return []
    finally:
        cursor.close()
        conexion.close()

def obtener_materias_profesor(clave_profesor):
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor(dictionary=True)
    try:
        query = """
            SELECT m.clave, m.nombre, m.grado
            FROM profesor_materia_grupo pmg
            JOIN materia m ON pmg.clave_materia = m.clave
            WHERE pmg.clave_profesor = %s
        """
        cursor.execute(query, (clave_profesor,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al obtener materias del profesor:", e)
        return []
    finally:
        cursor.close()
        conexion.close()

def insertar_grupo_alumno(claveAlumno,grado,grupo):
    conexion=crear_conexion()
    if not conexion:
        return False
    
    cursor=conexion.cursor()
    query="INSERT INTO grupo_alumno (clave_alumno,grado,grupo) VALUES(%s,%s,%s) "
    datos=(claveAlumno,grado,grupo)
    try:
        cursor.execute(query,datos)
        conexion.commit()
        return True
    
    except Exception as e:
        print("Error al insertar un grupo al alumno:",e)
        return 0
    
    finally:
        cursor.close()
        conexion.close()
    
    pass

def insertar_reporte(fecha, asunto, descripcion,claveAlumno, claveMateria):
    conexion= crear_conexion()
    if not conexion:
        return False
    
    cursor=conexion.cursor()
    query="INSERT INTO reporte (fecha,asunto,descripcion,clave_alumno,clave_materia) VALUES (%s,%s,%s,%s,%s) "
    datos=(fecha,asunto,descripcion,claveAlumno,claveMateria)

    try:
        cursor.execute(query,datos)
        conexion.commit()
        return True
    
    except Exception as e:
        print("Error al insertar un reporte:",e)
        return 0
    
    finally:
        cursor.close()
        conexion.close()

def buscar_reporte(id):
    conexion=crear_conexion()
    if not conexion:
        return False
    
    cursor=conexion.cursor()
    query="SELECT * FROM reporte WHERE id= %s"

    try:
        cursor.execute(query,(id,))
        fila=cursor.fetchone()

        if fila:
            return{
            "id":int(fila[0]),
            "fecha":  fila[1],
            "asunto":fila[2],
            "descripcion": fila[3],
            "claveAlumno":fila[4],
            "claveMateria":fila[5]
            }
        
        return None
       
    except Exception as e:
        print("Error al buscar reporte:",e)
        return False
    
    finally:
        cursor.close()
        conexion.close()

def borrar_reporte (id):
    conexion=crear_conexion()
    if not conexion:
        return False
    
    cursor=conexion.cursor()
    query="DELETE FROM reporte WHERE id=%s"

    try:
        cursor.execute(query, (id,))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al borrar el reporte: ",e)
        return False
    finally:
        cursor.close()
        conexion.close()


def mostrar_reporte(claveAlumno):

    conexion=crear_conexion()
    if not conexion:
        return False
    
    cursor=conexion.cursor()
    query="SELECT * FROM reporte WHERE clave_alumno=%s "

    try:
        cursor.execute(query,(claveAlumno,))
        filas = cursor.fetchall()
    
        reportes = []
        for fila in filas:
            reportes.append({
                "id": fila[0],
                "fecha": fila[1],
                "asunto": fila[2],
                "descripcion": fila[3],
                "claveAlumno": fila[4],
                "claveMateria": fila[5]
            })
        return reportes
    
    except Exception as e:
        print("Error al mostrar los reportes",e)
        return False
    
    finally:
        cursor.close()
        conexion.close()

def insertar_horario(materia, profesor, dia, inicio, fin, grupo):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = """
        INSERT INTO horario (clave_materia, clave_profesor, dia, hora_inicio, hora_fin, grupo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    datos = (materia, profesor, dia, inicio, fin, grupo)

    try:
        cursor.execute(query, datos)
        conexion.commit()
        return True
    except Exception as e:
        print("Error al insertar horario:", e)
        return False
    finally:
        cursor.close()
        conexion.close()
        
def consultar_horarios():
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor()
    query = "SELECT clave_materia, clave_profesor, dia, hora_inicio, hora_fin, grupo FROM horario"

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print("Error al consultar horarios:", e)
        return []
    finally:
        cursor.close()
        conexion.close()


def actualizar_horario(id_horario, materia, profesor, dia, inicio, fin, grupo):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = """
        UPDATE horario
        SET clave_materia = %s,
            clave_profesor = %s,
            dia = %s,
            hora_inicio = %s,
            hora_fin = %s,
            grupo = %s
        WHERE id = %s
    """
    datos = (materia, profesor, dia, inicio, fin, grupo, id_horario)

    try:
        cursor.execute(query, datos)
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al actualizar horario:", e)
        return False
    finally:
        cursor.close()
        conexion.close()

def eliminar_horario(id_horario):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = conexion.cursor()
    query = "DELETE FROM horario WHERE id = %s"

    try:
        cursor.execute(query, (id_horario,))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar horario:", e)
        return False
    finally:
        cursor.close()
        conexion.close()