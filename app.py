from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import *

app = Flask(__name__)
app.config.update(custom_db_config)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)