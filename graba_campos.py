''' FUNCION PASAR BASE DE CSV A B MYSQL  solo correr una vez'''

'''update campos_colombia set campo='Aposentos' where marcas='Blancas' AND patron=68.30 AND dis1=316;'''

from datetime import datetime, date, time, timedelta
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

class CamposCompletos:
    def __init__(self):
        self.lista=[]
    def iniciarCamposCompletos(self):
        archivo=open('campos_colombia.txt','a')
        archivo.close()
    def leerCamposCompletos(self):
        archivo=open('campos_colombia.txt', 'r')
        linea=archivo.readline()
        if linea:
            while linea:
                if linea[-1] =='\n':
                    linea = linea[:-1]
                self.lista.append(linea)
                linea=archivo.readline()
        archivo.close()
    def devolverlistado(self):
        listado=[]
        for elemento in self.lista:
            arreglo=elemento.split(';')
            listado.append(arreglo)
        return listado

def GrabarBaseCamposColombia(linea):
    dbconfig = read_db_config()
    q1="INSERT INTO campos_colombia (campo,marcas,patron,curva,par1,par2,par3,par4,par5,par6,par7,par8,par9,par10,par11,par12,par13,par14,par15,par16,par17,par18,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,dis11,dis12,dis13,dis14,dis15,dis16,dis17,dis18,ven1,ven2,ven3,ven4,ven5,ven6,ven7,ven8,ven9,ven10,ven11,ven12,ven13,ven14,ven15,ven16,ven17,ven18) VALUES ("
    q2="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    query=q1+q2
    try:
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # print(linea)
        cursor.execute(query,linea)
        conn.commit()
    except Error as error:
        dato='errror'
    finally:
        cursor.close()
        conn.close()


def main():
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
