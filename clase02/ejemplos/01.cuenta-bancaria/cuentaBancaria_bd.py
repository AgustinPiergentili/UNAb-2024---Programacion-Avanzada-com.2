import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Agustin1",
        database="CuentaBancaria"
    )

