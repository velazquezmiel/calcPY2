from peewee import AutoField, CharField, Model, ForeignKeyField, DoubleField
from config.database import database
from models.comodos import ComodoDB
from models.residencias import ResidenciaDB
class DispositivoDB(Model):
    id = AutoField()
    nome = CharField()
    consumo = DoubleField()
    uso_diario = DoubleField()
    comodo = ForeignKeyField(ComodoDB, backref='dispositivos')
    residencia = ForeignKeyField(ResidenciaDB, backref='dispositivos')

    class Meta:
        database = database
