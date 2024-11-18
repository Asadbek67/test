import psycopg2


conn = psycopg2.connect(
    dbname="dgango",
    user="postgres",
    password="a1100130a",
    host="localhost"
)


cursor = conn.cursor()




for  in :
    cursor.execute()


conn.commit()


cursor.close()
conn.close()
