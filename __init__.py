from flask import Flask 

app = flask(__name__)
app.config.from_object('settings')

from home import views
