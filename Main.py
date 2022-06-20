import psycopg2
from pyparsing import *
from Loadini import load

def connecta():
    global conn
    conn = None
    try:
        ini = load()
        conn = psycopg2.connect(*ini)
        cur = conn.cursor()

        comandoteste='SELECT from empregados;'
        cur.execute(comandoteste)
        lancacomando = cur.fetchall()
        print(lancacomando)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as errou:
        print(errou)


def leitura():
    file = open("teste02.txt", 'r')

    linhas = file.readlines()
    global data
    data=[]

    i=0
    for line in linhas:



        details = line.split(",")

        details = [x.strip() for x in details]
        details = [x.strip('<') for x in details]
        details = [x.strip('>') for x in details]

        #print(details)

        #Desgraca, aaaaaaaaaaaaaaaaaaaa, fazer funcionar e ver direito


        dets=Word(alphas)
        dets.parseString(details[0])
        #if data[i]=='End CKPT':
        #    print(data[i+1])
        data.append(details)
        print(dets)
        #parseString(details[i])
        if data[i]==("End CKPT"):
            break
        i=i+1








    #cur = conn.cursor()



def insercao():
    cur = conn.cursor()
    for i in range(len(data)):
        commands=['begin;', 'insert into empregados(id, name, value) values({data[i]});', 'commit;']

        cur.execute(commands)

def close():

    if conn != None:
            conn.close()
            print('Fechou.')




if name == 'main':
    connecta()
    leitura()
    #insercao()

    close()