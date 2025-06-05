
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:secure_password@localhost/employee_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False