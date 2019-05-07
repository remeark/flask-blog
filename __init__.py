from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.settings')
db = SQLAlchemy(app)

from flask_blog.home import views
from flask_blog.author import views
