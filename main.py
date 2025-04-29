from sqlalchemy import create_engine, Column, String, Integer, Boolean, column, ForeignKey, Delete
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando um banco de dados - create_engine
db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()


# Tabelas
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = 'livros'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtde_paginas = Column('qtde_paginas', Integer)
    dono = Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

# CRUD

# C - Create
#usuario = Usuario(nome='Pedro', email='pedro@email.com', senha='123456')
#session.add(usuario)
#session.commit()

# R - Read
#lista_usuarios = session.query(Usuario).all()
usuario_paulo = session.query(Usuario).filter_by(id=2).first()
print(usuario_paulo)
print(usuario_paulo.nome)
print(usuario_paulo.email)

#livro = Livro(titulo='Nome do vento', qtde_paginas=1000, dono=usuario_paulo.id)
#session.add(livro)
#session.commit()

# U - Update
#usuario_paulo.nome = 'pedro martins'
#session.add(usuario_paulo)
#session.commit()

# D - Delete
#session.delete(usuario_paulo)
#session.commit()
