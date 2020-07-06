from orm import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password = db.Column(db.String(20))
    gender = db.Column(db.Enum('male', 'female'), default='unknow')
    city = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.Date, default='1990-01-01')
    bio = db.Column(db.Text)
