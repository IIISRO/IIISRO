from flask import Flask


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/products_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

from extensions import *
from model import *
