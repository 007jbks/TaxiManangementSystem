import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.environ["s_host"],
        user=os.environ["s_user"],
        password=os.environ["s_pass"],
        database="defaultdb",
    )


def execute_query(query, params=None):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(query, params)
    db.commit()

    affected = cursor.rowcount

    cursor.close()
    db.close()
    return affected


def fetch_query(query, params=None):
    db = get_connection()
    cursor = db.cursor(dictionary=True)  # returns rows as dict

    cursor.execute(query, params)
    result = cursor.fetchall()

    cursor.close()
    db.close()
    return result
