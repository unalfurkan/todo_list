from sqlalchemy import create_engine


class Connect:
    def __init__(self):
        db_addr = input("DB ip address: ")
        db_user = input(f"Username of {db_addr}: ")
        db_pass = input(f"Password of {db_user}@{db_addr}: ")
        db_name = input("Database name to connect: ")

        url = f"mysql+pymysql://{db_user}:{db_pass}@{db_addr}/{db_name}"

        engine = create_engine(url, echo=True)

