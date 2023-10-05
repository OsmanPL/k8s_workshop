from flask import Flask, jsonify
from os import getenv
import mysql.connector


def registrar(nombre):
    conexion = mysql.connector.connect(
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        database=getenv("DB_DATABASE")
    )

    retorno = {"message": "Error al obtener registros", "server": "Python"}
    if conexion.is_connected():
        print("Conexión exitosa a MySQL")
        print(nombre)
        # Llamar al procedimiento almacenado
        cursor = conexion.cursor()
        query = "call registrar(%s)"
        cursor.execute(query, (nombre,))
        print("Inserted",cursor.rowcount,"row(s) of data.")
        retorno = {"message": "Registro creado", "server": "Python"}
        cursor.close()
        conexion.commit()
        conexion.close()

    return jsonify(retorno)

def getRegistros():
    data = []
    print(getenv("DB_HOST"))
    conexion = mysql.connector.connect(
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        database=getenv("DB_DATABASE")
    )
    # conectamos con la db para obtener el historial del pago de planilla
    # Comprobar si la conexión fue exitosa

    if conexion.is_connected():
        print("Conexión exitosa a MySQL")
        # Llamar al procedimiento almacenado
        cursor = conexion.cursor()
        cursor.callproc('getRegistros', [])

        for result in cursor.stored_results():
            data = result.fetchall()

        cursor.close()
        conexion.commit()
        conexion.close()
    data2 = []

    for i in data:
        id = i[0]
        name = i[1]
        fecha_hora = i[2]
        data2.append(
            {"id": id, "nombre": name, "fecha_hora":fecha_hora })
    retorno = {"server": "python", "registros": data2}

    return jsonify(retorno)
