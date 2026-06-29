from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
    avatar = Column(String)

    admin = Column(
        Boolean,
        default=False
    )


class Tema(Base):
    __tablename__ = "temas"

    id = Column(Integer, primary_key=True)
    nome = Column(String)

    liberado = Column(Boolean, default=False)


class Pergunta(Base):
    __tablename__ = "perguntas"

    id = Column(Integer, primary_key=True, index=True)
    enunciado = Column(String)
    tipo = Column(String)
    tema_id = Column(Integer)


class Alternativa(Base):
    __tablename__ = "alternativas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    correta = Column(Boolean)
    pergunta_id = Column(Integer)


class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer)
    total = Column(Integer)
    acertos = Column(Integer)
    erros = Column(Integer)
    percentual = Column(Integer)
    tentativa_id =Column(Integer)

class Tentativa(Base):
    __tablename__ = "tentativas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    usuario_id = Column(
        Integer
    )

    concluida = Column(
        Boolean,
        default=False
    )

class Resposta(Base):
    __tablename__ = "respostas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer)
    pergunta_id = Column(Integer)
    alternativa_id = Column(Integer)
    tentativa_id = Column(Integer)

class Auditoria(Base):

    __tablename__ = "auditoria"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    usuario_id = Column(
        Integer
    )

    acao = Column(
        String
    )

    data_hora = Column(
        DateTime,
        default=datetime.now
    )