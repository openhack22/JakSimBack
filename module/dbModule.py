from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.String(25), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    money_plus = db.Column(db.Integer, nullable=False)
    money_minus = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    # 임시 코드
    def __repr__(self):
        return f"<User('{self.id}', '{self.username}', '{self.email}')>"


class Goal(db.Model):
    __table_name__ = 'goal'

    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goal_name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Enum, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user_limit = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)  # True: 진행중, False: 준비중
    description = db.Column(db.Text, nullable=True)


class Team(db.Model):
    __table_name__ = 'team'

    goal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    image = db.Column(db.Text, nullable=False)  # image url
