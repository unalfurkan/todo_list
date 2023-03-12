from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


def add_todo(todo: str):
    engine = create_engine('mysql+pymysql://root:isThisWeak!@localhost/todo_db', echo=True)
    metadata = MetaData()
    table = Table('todolist', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('todo', String))

    conn = engine.connect()
    trans = conn.begin()

    try:
        new_todo = {'todo': todo}
        conn.execute(table.insert(), new_todo)
        trans.commit()
    except:
        trans.rollback()
        raise
    finally:
        conn.close()


