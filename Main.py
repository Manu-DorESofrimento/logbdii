import psycopg2
from Loadini import load

def connecta():
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
    finally:
        #Remover fechamento da conexão e dar um jeito aqui
        if conn != None:
            conn.close()
            print('Fechou.')

def leitura():
    print("vrum")

if __name__ == '__main__':
    connecta()
    leitura()