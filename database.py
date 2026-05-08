from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Esta es la tabla que guardará tus conversiones para el historial
class Conversion(Base):
    __tablename__ = 'conversiones'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    funcion = Column(String)
    valor_entrada = Column(Float)
    valor_salida = Column(Float)

# Esta es la función que te falta (get_engine)
def get_engine():
    return create_engine('sqlite:///conversiones.db')

def init_db(engine):
    Base.metadata.create_all(engine)

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()