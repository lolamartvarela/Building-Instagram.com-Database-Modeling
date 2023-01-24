import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre_de_usuario = Column(String(250), nullable=False)
    nombre = Column(String(50))
    apellido = Column(String(50))
    email = Column(String(100), nullable=False)


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    usuario_id = Column (Integer, ForeignKey('usuario.id'))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(350))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    url = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
