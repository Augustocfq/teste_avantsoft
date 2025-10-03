from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

custom_db_config: dict = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///students.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}