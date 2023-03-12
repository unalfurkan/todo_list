from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


def remove_task(task_id: int):
    engine = create_engine('mysql+pymysql://root:isThisWeak!@localhost/todo_db', echo=True)
    metadata = MetaData()
    table = Table('tasks', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('task_name', String))

    conn = engine.connect()
    trans = conn.begin()

    try:
        conn.execute(table.delete().where(table.c.id == task_id))
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()
