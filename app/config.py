import os

class Config:
    SECRET_KEY = os.urandom(24)  # Chave secreta para sessões
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/crud_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
