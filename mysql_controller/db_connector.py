"""
this script will create a mysql connection and return requested items
"""

# TODO data migration konusunu öğren

# TODO sqlalchemy

# https://www.youtube.com/watch?v=3vsC05rxZ8c&ab_channel=TechWithTim
import os

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="isThisWeak!",
)
#
# db = mysql.connector.connect(
#     host=os.getenv("MYSQL_HOST"),
#     user=os.getenv("MYSQL_USER"),
#     password=os.getenv("MYSQL_PASSWORD")
# )


db_cursor = db.cursor()

db_cursor.execute("CREATE DATABASE test_from_code")
