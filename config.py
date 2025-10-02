from flask import Config

custom_db_config: dict = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///students.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}