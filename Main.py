import psycopg2
from Loadini import load

def connecta():
    global conn
    conn = None
    try:
        ini = load()
        conn = psycopg2.connect(**ini)
        cur = conn.cursor()
        
        comandoteste='SELECT * from empregados;'
        cur.execute(comandoteste)
        lancacomando = cur.fetchall()
        print(lancacomando)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as errou:
        print(errou)
        

def leitura():
    file = open("teste02.txt", 'r')

    linhas = file.readlines()
    data=[]
    


    for line in reversed(linhas):

        

        details = line.split(",")
        details = [x.strip() for x in details]
        details = [x.strip('<') for x in details]
        details = [x.strip('>') for x in details]
        details = [x.strip(']') for x in details]
        
        print(details)
        
        #Desgraca, aaaaaaaaaaaaaaaaaaaa, fazer funcionar e ver direito
        data.append(details)
        #print(data)
        if details==("End CKPT"):
            break
    


        
    


    #cur = conn.cursor()

def close():

    if conn != None:
            conn.close()
            print('Fechou.')

if __name__ == '__main__':
    connecta()
    leitura()
    close()