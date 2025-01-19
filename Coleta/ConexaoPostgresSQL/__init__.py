import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="dataWh",
    user="postgres",
    password="1234"
)

def conecxaoPostgres():
    cur = conn.cursor()
    cur.execute('SELECT * FROM Dados_Nasa')
    rows = cur.fetchall()

    for row in rows:
        print(row)