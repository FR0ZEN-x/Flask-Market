# # This file is used to create the database and add initial data.
#
# from market.models import db, Item  # Import the db and Animal class from basic.py
# from market import app
#
# with app.app_context():  # Ensure the app context is available
#     db.create_all()  # Create the table structure (schema) in the database
#
#     item1  = Item(name="Phone", price=500, barcode="893212299897", description="New iPhone 10")
#     item2  = Item(name="Laptop", price=900, barcode="123985473165", description="New MacBook Air")
#     item3  = Item(name="Keyboard", price=150, barcode="231985128446", description="Wired keyboard")
#
#     db.session.add_all([item1, item2, item3])  # Add the instances as database rows
#     db.session.commit()  # Commit the changes to the database
#
#     # Item.query.all()  # Return a list of all the rows in the table
#
