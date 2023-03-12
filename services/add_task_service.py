from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


def add_task(task_name: str):
    engine = create_engine('mysql+pymysql://root:isThisWeak!@localhost/todo_db', echo=True)
    metadata = MetaData()
    table = Table('tasks', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('task_name', String))

    conn = engine.connect()
    trans = conn.begin()

    try:
        new_task = {'task_name': task_name}
        conn.execute(table.insert(), new_task)
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()
