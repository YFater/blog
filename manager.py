#!/usr/bin/env python

from flask import Flask, redirect

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from article.views import article_bp
from orm import db
from user.views import user_bp

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yf:YUANfen13!@47.100.84.210:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '110'

db.init_app(app)


manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

app.register_blueprint(user_bp)
app.register_blueprint(article_bp)

@app.route('/')
def home():
    return redirect('/article/show_articles')

if __name__ == "__main__":
    manager.run()
