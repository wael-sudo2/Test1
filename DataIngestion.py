import json
import pymysql
import time

DATA_FILE_NAME = "data.json"

time.sleep(30) # waiting time for mysql container to run 

with open('data.json', 'r') as f:
    data = json.load(f)


conn = pymysql.connect(host='mysql', user='root', password='test1pw', port=3306, database='extracted_data',)
cursor = conn.cursor()

with open('database_schema.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.execute(sql_script)

for item in data:
    cursor.execute('INSERT INTO extracted_data (name, price, brand, imageUrl, productUrl) VALUES (%s, %s, %s, %s, %s)',
                   (item['name'], item['price'], item['brand'], item['imageUrl'], item['productUrl']))

conn.commit()
conn.close()
