
from datetime import datetime, date, time, timedelta
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

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

def existeNetos(numero_juego,jugador):
    query=" SELECT campo FROM netos_stableford WHERE numero_juego = %s AND jugador = %s "
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
def creaNetos(tarjeta):
    dbconfig = read_db_config()
    q1="INSERT INTO netos_stableford (numero_juego,grupo,jug,jugador,nombre,campo,net1,net2,net3,net4,net5,net6,net7,net8,net9,net10,net11,net12,net13,net14,net15,net16,net17,net18,n_ida,n_vuelta,n_total,stb1,stb2,stb3,stb4,stb5,stb6,stb7,stb8,stb9,stb10,stb11,stb12,stb13,stb14,stb15,stb16,stb17,stb18,stb_ida,stb_vuelta,stb_total) VALUES ("
    q2="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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
def cambiadatotalNetos(numero_juego,grupo,jug,dato,valor):
    dbconfig = read_db_config()
    q1="UPDATE netos_stableford SET "
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
def recuperaNetos(numero_juego):
    query=" SELECT * FROM netos_stableford WHERE numero_juego= %s "
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

def ordenmenormayor(lista,pos):
    largo=len(lista)
    for i in range(largo):
        for j in range((i+1),largo):
            fila1=lista[i]
            fila2=lista[j]
            if fila1[pos]<fila2[pos]:
                continue
            else:
                lista[i]=fila2
                lista[j]=fila1
    return lista
def ordenmayormenor(lista,pos):
    largo=len(lista)
    for i in range(largo):
        for j in range((i+1),largo):
            fila1=lista[i]
            fila2=lista[j]
            if fila1[pos]>fila2[pos]:
                continue
            else:
                lista[i]=fila2
                lista[j]=fila1
    return lista

def main():
    resnetos=recuperaNetos(numero_juego=46)
    # nresnetos=ordenmenormayor(lista=resnetos,pos=25)
    nresnetos=ordenmayormenor(lista=resnetos,pos=45)
    for linea in nresnetos:
        print(linea[4])
        print(linea[45])

    # lista=[[1,1,1,'juan',35,35,70],[1,1,2,'pedro',37,40,77],[1,2,1,'maria',33,40,73],[1,2,2,'liliana',41,38,79],[1,3,1,'gabriel',39,33,72],[1,3,2,'ramiro',36,36,72]]
    # print(loquesea)
    # print(loquesea[1])
    # copialoquesea=loquesea
    # print(copialoquesea)
    # copialoquesea[0]=loquesea[5]
    # print(copialoquesea)
    # pos=4
    # largo=len(lista)
    # for i in range(largo):
    #     for j in range((i+1),largo):
    #         fila1=lista[i]
    #         fila2=lista[j]
    #         if fila1[pos]<fila2[pos]:
    #             continue
    #         else:
    #             lista[i]=fila2
    #             lista[j]=fila1
    # print(lista)
    # nlista=ordenmenormayor(lista=lista,pos=6)
    # print(nlista)


#**************************
    # numero_juego=38
    # tarjetas=recuperaTodasTarjetasJuegoGolf(numero_juego=numero_juego)
    # for tarjeta in tarjetas:
    #     grupo=tarjeta[50]
    #     jug=tarjeta[51]
    #     jugador=tarjeta[2]
    #     nombre=tarjeta[52]
    #     campo=tarjeta[4]
    #     netos0=[numero_juego,grupo,jug,jugador,nombre,campo,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #     # print(netos0)
    #     creaNetos(tarjeta=netos0)
#***********************
    # marcas=recuperaMarcasCampos(campo="Serrezuela")
    # print(marcas)
#***************************************
    # indice=float(datotalUsuarios(co='alejoml@live.com',tal="indice"))
    # curva=datotalCampos(campo="Serrezuela",marcas="Azules",tal="curva")
    # print(curva)
    # print('su indice')
    # print(indice)
    # handi=(indice*curva/113)
    # print('su handi')
    # print(handi)
    # enhandi=int(handi)
    # residuo=handi-enhandi
    # if residuo>=0.5:
    #     handicap=enhandi+1
    # else:
    #     handicap=enhandi
    # print('Su handicap:')
    # print(handicap)
    # archivo=CamposCompletos()
    # archivo.leerCamposCompletos()
    # listado=archivo.devolverlistado()
    # for parte in listado:
    #     parte[2]=float(parte[2])
    #     for i in range(3,58):
    #         parte[i]=int(parte[i])
    #     # print(parte)
    #     GrabarBaseCamposColombia(linea=parte)
    # # print(listado[0])


if __name__ == '__main__':
    main()
