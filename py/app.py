import mariadb
import dbcreds

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

cursor.execute("CALL proceedure_1('client3', 'client3@test.com', '125 fake street')")
results = cursor.fetchall()

cursor.close()
conn.close()

print(results)