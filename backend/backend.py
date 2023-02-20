"""
This script will handle creating and deleting tasks
"""
# from mysql_controller import db_connection_manager
from sqlalchemy import text, create_engine, URL
url_object = URL.create(
    'mysql',
    username="root",
    password="isThisWeak!",
    host="3306",
    database="todo_db"
)

def create_task():
    print("task create")
    # engine = db_connection_manager.Connect()
    engine = create_engine(url_object)
    with engine.connect() as connection:
        result = connection.execute(text("select * from tasks"))
        print(result)


def delete_task():
    print("task delete")


def create_todo():
    print("subtask create")


def delete_todo():
    print("subtask edit")
