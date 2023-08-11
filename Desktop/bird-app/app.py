import os
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource


from flask import request, session as flask_session
from sqlalchemy.sql import text
from sqlalchemy import event
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask_bcrypt import Bcrypt

# from models import db, Bird
from models import db, User, Product, Transaction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
flask_bcrypt=Bcrypt(app)
app.secret_key="hello"
SESSION_TYPE="sqlalchemy"
CORS(app)

# class Birds(Resource):

#     def get(self):
#         birds = [bird.to_dict() for bird in Bird.query.all()]
#         return make_response(jsonify(birds), 200)

# api.add_resource(Birds, '/birds')

@app.route('/')
def home(): 
    return {}

@app.route('/session')
def session():
    user = User.query.filter(User.id==flask_session.get('user.id')).first()
    if not user:
        return {'error':'Please login'},401
    return user.to_dict()

@app.route('/login', methods = ['POST'])
def login():
    print(request.json)
    error_message = {'error': 'username/password not on file'}
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter(User.username == username).first()
    if not user: 
        return error_message, 401
    if not user.password:
        return error_message, 401
    flask_session['user_id'] = user.id 
    return user.to_dict()




@app.route('/user', methods = ['POST'])
def register_new_user():
    if (request.method == 'POST'):
        data = request.json 
        user = User()
        try: 
            for attr in data:
                setattr(user, attr, data[attr])
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 201 
        except (IndentationError, ValueError) as ie:
            return {'error' : ie.args}, 422
            
        
    
@app.route('/user/<int:id>', methods = ['GET','PATCH'])
def edit_user(id):
    user = User.query.filter(User.id == id).first()
    if not user:
        return {'error' : 'user not found'}, 404
    
    if(request.method == 'PATCH'):
        data = request.json 
        try: 
            for attr in data: 
                setattr(user, attr, data[attr])
            db.session.commit()
            return user.to_dict(rules = ('-transactions',)), 200
        except (IntegrityError, ValueError) as ie: 
            return {'errors': ie.args}, 422 
        
    return user.to_dict(rules = ('-transactions',))

@app.route('/products', methods=["GET"])
def products():
    if(request.method=="GET"):
        all=Product.query.all()
        products=[]
        for product in all:
            products.append(product.to_dict())
        return products
    

@app.route('/transactions', methods=["GET"])
def transactions():
    if(request.method=="GET"):
        all=Transaction.query.all()
        transactions = []
        for transaction in all:
            transactions.append(transaction.to_dict())
        return transactions[(len(transactions) -1)]
    
@app.route('/checkout', methods=["POST"])
def checkout():
    if(request.method=="POST"):
        data = request.json
        user = data['user_id']
        products = data['products']
        transaction_id = data['transaction_id']
        return_list = []
        for product in products:
            try:
                transaction = Transaction()
                setattr(transaction, "user_id", user)
                setattr(transaction, "transaction_code", transaction_id)
                setattr(transaction, "product_id", product['id'])
                db.session.add(transaction)
                db.session.commit()
                return_list.append(transaction.to_dict())
            except(IntegrityError, ValueError) as ie:
                return {"error":ie.args},422
        return {"success":"Transaction completed successfully"},201


@app.route("/logout",methods=["DELETE"])
def logout():
    flask_session['user_id']=None
    return {},204


# if __name__ == '__main__':
#     app.run(port=10000, debug=True)

# def getApp():
#     return app
