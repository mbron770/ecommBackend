from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# class Bird(db.Model, SerializerMixin):
#     __tablename__ = 'birds'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     species = db.Column(db.String)

#     def __repr__(self):
#         return f'<Bird {self.name} | Species: {self.species}>'


class User(db.Model, SerializerMixin):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String,nullable=False)
    lname=db.Column(db.String,nullable=False)
    username=db.Column(db.String,nullable=False,unique=True)
    # _password_hash=db.Column(db.String,nullable=False)
    password=db.Column(db.String, nullable = False)
    address=db.Column(db.String, nullable = False)
    
    transactions = db.relationship('Transaction', back_populates = 'user')
    
    serialize_rules = ('-transactions.user',)
    
    # hash password and authenticate password 
    
    # @hybrid_property 
    # def password_hash(self): 
    #     raise ValueError('Password hash is private')
    
    # @password_hash.setter
    # def password_hash(self, password):
    #     self._password_hash=flask_bycrypt.generate_password_hash(password).decode('utf-8')
    
    # def authenticate(self, password): 
    #     return flask_bycrypt.check_password_hash(self._password_hash, password)
    
    
    
    
class Product(db.Model, SerializerMixin): 
    __tablename__='products'
    id=db.Column(db.Integer, primary_key=True)
    product_name=db.Column(db.String, nullable = False)
    product_category=db.Column(db.String, nullable = False)
    price=db.Column(db.Double, nullable = False)
    product_quantity=db.Column(db.Integer, nullable = False)
    image=db.Column(db.String, nullable = False)
    
    transactions = db.relationship('Transaction', back_populates = 'product')
    
    serialize_rules = ('-transactions.product',)
    
# class Transaction(db.Model, SerializerMixin):
#     __tablename__='transactions'
#     id = db.Column(db.Integer, primary_key = True)
#     # transaction_amount=db.Column(db.Double, nullable = False) 
#     transaction_date=db.Column(db.DateTime, default = db.func.now())
#     transaction_code = db.Column(db.Integer, nullable = False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
#     user = db.relationship('User', back_populates = 'transactions')
#     product = db.relationship('Product', back_populates = 'transactions')
    
#     serialize_rules = ('-user.transactions', '-product.transactions')
    
    
    
class Transaction(db.Model, SerializerMixin):
    __tablename__='transactions'
    id = db.Column(db.Integer, primary_key=True) 
    transaction_date=db.Column(db.DateTime, default = db.func.now())
    transaction_code = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
    user = db.relationship('User', back_populates = 'transactions')
    product = db.relationship('Product', back_populates = 'transactions')
    
    serialize_rules = ('-user.transactions', '-product.transactions')
