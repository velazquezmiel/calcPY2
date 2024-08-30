from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def startup_db():
    from models.residencias import ResidenciaDB
    from models.comodos import ComodoDB
    from models.dispositivos import DispositivoDB

    database.connect()
    database.create_tables([ResidenciaDB, ComodoDB, DispositivoDB])

def shutdown_db():
    database.close()