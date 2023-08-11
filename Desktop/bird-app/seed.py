# from app import app
# from models import db, Bird

# with app.app_context():

#     print('Deleting existing birds...')
#     Bird.query.delete()

#     print('Creating bird objects...')
#     chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
#     grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
#     starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
#     dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

#     print('Adding bird objects to transaction...')
#     db.session.add_all([chickadee, grackle, starling, dove])

#     print('Committing transaction...')
#     db.session.commit()

#     print('Complete.')
    
    
    
    
from app import app
from models import db, User, Product, Transaction
from faker import Faker
import random

fake = Faker()

with app.app_context():
    def random_3_digits():
        return str(random.randint(100, 999))

    def random_price():
        return round(random.uniform(1, 999), 2)

    db.drop_all()
    db.create_all()

    arr = [1, 1, 1, 1, 1, 6, 7, 8, 9, 10]
    product_names = ['iRobot Roomba 694 Robot Vacuum',
                     'Amazon Fire TV Stick 4K',
                     'Bialetti Express Moka Pot (6 -Cup)',
                     'Amazon Echo Dot 5th Gen',
                     'Lodge Cast Iron Skillet',
                     'Ring Video Doorbell',
                     'DASH Mini Maker for Waffles',
                     'Saucemoto Dip Clip',
                     'LEVOIT Core 300 Air Purifier',
                     'AmazonBasics Silicone Baking Mat',
                     'elago 3-in-1 Charging Station',
                     'Stanley Stainless Steel Tumbler'









                     ]

    product_images = ['https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1664908138-41iDzC2UOzL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1636118032-31Jh6teontL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1683125208-51I5yOJUkfL.jpg?crop=1xw:0.886xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1664420477-51lUym-OXcL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',

                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1550087291-41UPePLXEkL.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1618945586-31QGyzXLgrL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1677180010-31vsETJ-6FL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1684956299-7115AWGe76L.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1634586655-416YAMWP4bL._SL500_.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1550087229-silicone-mat-best-selling-amazon-products-1550087211.jpg?crop=1xw:1xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1688677167-51Ly3UnlOuL.jpg?crop=1xw:1.00xh;center,top&resize=980:*',
                      'https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1688654131-screen-shot-2023-07-06-at-10-29-13-am-64a6cfc86390d.png?crop=0.889xw:1.00xh;0.111xw,0&resize=980:*'






                      ]
    product_price = [249.00, 50.00, 38.00,
                     23.00, 20.00,
                     100.00,
                     20.00,
                     11.00,
                     105.00,
                     14.00,
                     30.00,
                     49.00


                     ]
    users = {}
    products = {}

    for i in range(10):
        user = User(
            fname=fake.first_name(),
            lname=fake.last_name(),
            username=random_3_digits(),
            password=random_3_digits(),
            address=fake.address()
        )
        db.session.add(user)
        db.session.commit()  # Commit to get the id
        users[user.id] = user

    for i in range(12):
        product_quantity = fake.random_int(min=1, max=100)
        # product_category=fake.word()
        product = Product()
        setattr(product, "product_name", product_names[i])
        setattr(product, "price", product_price[i])
        setattr(product, "product_category", 'Amazon top 12')
        setattr(product, "image", product_images[i])
        setattr(product, 'product_quantity', product_quantity)
        db.session.add(product)
        db.session.commit()

    for a in arr:
        transaction = Transaction(
            user_id=a,
            product_id=fake.random_int(min=1, max=10),
            transaction_code=fake.random_int(min=1, max=3)
        )
        db.session.add(transaction)

    db.session.commit()

    print('db seeded')


