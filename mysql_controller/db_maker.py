from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


class Create:
    # db_addr = input("DB ip address: ")
    # db_user = input(f"Username of {db_addr}: ")
    # db_pass = input(f"Password of {db_user}@{db_addr}: ")  # TODO convert this to getpass
    # db_name = input("Database name to connect: ")
    #
    uri = 'mysql+pymysql://root:isThisWeak!@localhost/todo_db'
    engine = create_engine(uri, echo=True)

    if not database_exists(engine.url):
        create_database(engine.url)
        from sqlalchemy import Table, Column, Integer, String, MetaData
        meta = MetaData()

        tasks = Table(
            'tasks', meta,
            Column('id', Integer, primary_key=True),
            Column('task_name', String(1024)),
        )
        todolist = Table(
            'todolist', meta,
            Column('id', Integer, primary_key=True),
            Column('todo', String(1024))
        )
        meta.create_all(engine)

    else:
        print("Given DB already exists...")
        engine.connect()
