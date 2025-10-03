from flask import Flask
from config import *
from api import *

app = Flask(__name__)
app.config.update(custom_db_config)
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(student_route)

if __name__ == '__main__':
    app.run(debug=True)