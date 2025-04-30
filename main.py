from sys import exception

from sqlalchemy import create_engine, Column, String, Integer, Boolean, column, ForeignKey, Delete
from sqlalchemy.orm import sessionmaker, declarative_base
import customtkinter as ctk

ctk.set_appearance_mode('dark')


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
usuario = Usuario
def validar_dados():
    nome = campo_nome.get()
    email = campo_email.get()
    senha = campo_senha.get()

    if not nome or not email or not senha:
        resultado_criar.configure(text='Todos os campos devem ser preenchidos')
        return
    novo_usuario = usuario(nome=nome, email=email, senha=senha)

    try:
        session.add(novo_usuario)
        session.commit()
        resultado_criar.configure(text='Usuario cadastrado com sucesso')
    except exception as e:
        session.rollback()
        resultado_criar.configure(text='Erro ao cadastrar usucario {}'.format(e))


# R - Read
#lista_usuarios = session.query(Usuario).all()
#usuario_paulo = session.query(Usuario).filter_by(id=2).first()
#print(usuario_paulo)
#print(usuario_paulo.nome)
#print(usuario_paulo.email)

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

# Criação da janela principal
app = ctk.CTk()
app.title('Banco de Dados')
app.geometry('300x500')


# Criação dos campos

# Criação do titulo
label_criar = ctk.CTkLabel(app, text='CREATE', font=('Helvetica', 14, 'bold'))
label_criar.pack(pady=10)

# label - nome
label_nome = ctk.CTkLabel(app, text='Nome')
label_nome.pack(pady=0)

# Entry - nome
campo_nome = ctk.CTkEntry(app, placeholder_text='Nome')
campo_nome.pack(pady=0)

# Label - email
label_email = ctk.CTkLabel(app, text='Email')
label_email.pack(pady=0)

# Entry - email
campo_email = ctk.CTkEntry(app, placeholder_text='Email')
campo_email.pack(pady=0)

# label - senha
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=0)

# Entry - Senha
campo_senha = ctk.CTkEntry(app, placeholder_text='Senha')
campo_senha.pack(pady=0)

# button Create
botao_criar = ctk.CTkButton(app, text='Create',command=validar_dados)
botao_criar.pack(pady=10)

# Campo feedback de criação
resultado_criar = ctk.CTkLabel(app, text='')
resultado_criar.pack(pady=10)

# Inicia o loop da aplicação ( Tela )
app.mainloop()

