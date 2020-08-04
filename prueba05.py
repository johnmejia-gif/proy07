''' FUNCIONES JUEGO DE GOLF '''
from datetime import datetime, date, time, timedelta
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def creaListaJuegos(campo,fec,modalidad,co):
    dbconfig = read_db_config()
    q1="INSERT INTO lista_juegos (campo,jugadores,fecha,modalidad,creador) VAlUES ("
    q2=")"
    query=q1+"%s"+",0,"+"%s"+","+"%s"+","+"%s"+q2
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        data=(campo,fec,modalidad,co)
        cursor.execute(query,data)
        conn.commit()
    except Error as error:
        dato='errror'
    finally:
        cursor.close()
        conn.close()
def ultimoJuegoCreado():
    query="SELECT max(numero_juego) from lista_juegos;"
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)
        num_juego=cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return num_juego[0]
def creaTarjetaJuegoGolf(tarjeta):
    dbconfig = read_db_config()
    q1="INSERT INTO tarjetas_golf (fecha, hora, jugador, marcador, campo, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12 ,h13 ,h14 ,h15 ,h16 ,h17 ,h18 ,ida, vuelta ,total ,firma_jugador, firma_marcador, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p_ida, p_vuelta, p_total, numero_juego, grupo, jug, nombre, handicap,marcas) VALUES ("
    q2="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    query=q1+q2
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,tarjeta)
        conn.commit()
    except Error as error:
        dato='errror'
    finally:
        cursor.close()
        conn.close()
def existeTarjetaJuegoGolf(numero_juego,grupo,jug):
    query=" SELECT campo FROM tarjetas_golf WHERE numero_juego = %s AND grupo = %s AND jug = %s "
    data=(numero_juego,grupo,jug)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        row=cursor.fetchone()

        if row is not None:
            encontrado='si'
            row=cursor.fetchone()
        else:
            encontrado='no'
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return encontrado
def existeJugadorTarjetaJuegoGolf(numero_juego,jugador):
    query=" SELECT campo FROM tarjetas_golf WHERE numero_juego = %s AND jugador = %s "
    data=(numero_juego,jugador)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        row=cursor.fetchone()
        if row is not None:
            encontrado='si'
            row=cursor.fetchone()
        else:
            encontrado='no'
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return encontrado
def cambiadatotalTarjetaJuegoGolf(numero_juego,grupo,jug,dato,valor):
    dbconfig = read_db_config()
    q1="UPDATE tarjetas_golf SET "
    q2= " = %s WHERE numero_juego = %s AND grupo=%s AND jug=%s "
    query=q1+dato+q2
    data=(valor,numero_juego,grupo,jug)
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        conn.commit()
    except Error as error:
        dato='errror'
    finally:
        cursor.close()
        conn.close()
def recuperaJugadorTarjetasJuegoGolf(numero_juego,grupo,jug):
    query=" SELECT jugador FROM tarjetas_golf WHERE numero_juego= %s AND grupo = %s AND jug=%s "
    data=(numero_juego,grupo,jug)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        extraccion=cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return extraccion[0]
def recuperaListaJuegos(numero_juego):
    query=" SELECT * FROM lista_juegos WHERE numero_juego= %s "
    data=(numero_juego,)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        extraccion=cursor.fetchone()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return extraccion
def recuperaTodasTarjetasJuegoGolf(numero_juego):
    query=" SELECT * FROM tarjetas_golf WHERE numero_juego= %s "
    data=(numero_juego,)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        tarjetas=cursor.fetchall()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return tarjetas
def recuperaTarjetasGrupoJuegoGolf(numero_juego,grupo):
    query=" SELECT * FROM tarjetas_golf WHERE numero_juego= %s AND grupo= %s"
    data=(numero_juego,grupo)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        tarjetas=cursor.fetchall()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return tarjetas
def recuperaNumerojugeoTarjetasJuegoGolf(fecha,jugador):
    query=" SELECT numero_juego FROM tarjetas_golf WHERE fecha= %s AND jugador= %s"
    data=(fecha,jugador)
    dbconfig = read_db_config()
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        nums_juegos=cursor.fetchall()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return nums_juegos


def consultadatoAgendaGolf(clu,cam,fec,tur,dato):
    q1=" SELECT "
    q2=" FROM agenda_golf WHERE club=%s AND campo=%s AND fecha = %s AND turno=%s "
    query=q1+dato+q2
    data=(clu,cam,fec,tur)
    dbconfig = read_db_config()
    hora:''
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query,data)
        row=cursor.fetchone()
        hora=row[0]
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    return hora

def main():
    nums_juego=recuperaNumerojugeoTarjetasJuegoGolf(fecha="2020-08-13",jugador="liliana uribe")
    cant_juegos=len(nums_juego)
    print(nums_juego)
    print(cant_juegos)
#******************
    # listajuego=recuperaListaJuegos(numero_juego=7)
    # campo=listajuego[1]
    # modalidad=listajuego[4]
    # print(campo)
    # print(modalidad)
#**********
    # encontrado=existeJugadorTarjetaJuegoGolf(numero_juego=10,jugador='jcmejia@live.com')
    # print(encontrado)
#**************
    # tarjetas=recuperaTodasTarjetasJuegoGolf(numero_juego=13)
    # print(len(tarjetas))
    # for i in range(len(tarjetas)):
    #     print(tarjetas[i])
    # for tarjeta in tarjetas:
    #     print(tarjeta[50])
    #     print(tarjeta[52])
    #     print(tarjeta[54])
    #     print(tarjeta[53])
#****************
    # jugador= recuperaJugadorTarjetasJuegoGolf(numero_juego=1,grupo=1,jug=4)
    # print(jugador)
#*************
    # cambiadatotalTarjetaJuegoGolf(numero_juego=1,grupo=1,jug=4,dato="Jugador",valor="Williams")
#**************
    # existe=existeTarjetaJuegoGolf(numero_juego=1,grupo=1,jug=5)
    # print(existe)
#*****************
    # numero_juego=4
    # grupo=1
    # jug=4
    # nombre="dagoberto"
    # handicap=4
    # tarjeta=["2020-08-02","0:00",nombre,"","Serrezuela",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"","",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,numero_juego,grupo,jug,nombre,handicap,"Blancas"]
    # print(tarjeta)
    # print(len(tarjeta))
    # creaTarjetaJuegoGolf(tarjeta)
#****************
    # num_juego=ultimoJuegoCreado()
    # print('el último juego creado es el número: ')
    # print(num_juego)

#    creaListaJuegos(campo="Serrezuela",fec="2020-07-27",modalidad="stroke play",co="mario@hot.com")


if __name__ == '__main__':
    main()
