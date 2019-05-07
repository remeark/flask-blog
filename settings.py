import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'malmeida'
DB_PASSWORD = '12345'
BLOG_DATABASE_NAME = 'flask_blog'
DB_URI = "postgresql+psycopg2://@/{0}".format('flask_blog')
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
