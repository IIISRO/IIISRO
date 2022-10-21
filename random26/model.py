from datetime import datetime
from extensions import db
from app import app

class Categories(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),unique=True)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return f'{self.title})'
    def __init__(self,title):
        self.title=title
    def save(self):
        db.session.add(self)
        db.session.commit()

class Products(db.Model):
    __tablename__='Products'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=True)
    description=db.Column(db.Text,nullable=True)
    amount=db.Column(db.Integer,default=0)
    price=db.Column(db.Float,default=0.00)
    production_date=db.Column(db.Integer)
    is_new=db.Column(db.Boolean,default=False)
    rating=db.Column(db.Float,db.CheckConstraint('rating>0'),default=0.0)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
    
    def __repr__(self):
        return f'{self.name})'
    def __init__(self,name,description,amount,price,production_date,is_new,rating,category_id):
        self.name=name
        self.description=description
        self.amount=amount
        self.price=price
        self.production_date=production_date
        self.is_new=is_new
        self.rating=rating
        self.category_id=category_id    
    def save(self):
        db.session.add(self)
        db.session.commit()


