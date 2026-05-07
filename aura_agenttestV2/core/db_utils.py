import pymysql
from dbutils.pooled_db import PooledDB

class MySQLClient:
    _pool = None

    def __init__(self):
        if not MySQLClient._pool:
            MySQLClient._pool = PooledDB(
                creator=pymysql,
                host="127.0.0.1",
                user="root",
                password="root",
                database="test",
                charset="utf8mb4",
                maxconnections=5,
                ping=1
            )

    def fetch(self, sql, args=None):
        conn = self._pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, args)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res