from flask import Flask

app = Flask(__name__, template_folder='Template', static_folder="Static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/bookshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'myproject'

from controller import *
from extensions import *
from models import *

if __name__ == "__main__":
    app.init_app(db)
    app.init_app(migrate)
    app.run(port = 5000, debug=True)