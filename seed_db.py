# seed_db.py
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from agent_app.models import Base, Customer, Product, Order

# Connect to the Docker service name 'postgres-db' instead of 'localhost'
DATABASE_URL = "postgresql://katalyst:12345@postgres-db:5432/katalystdb"

def seed_database():
    # Add a retry loop to handle timing
    for i in range(10):
        try:
            engine = create_engine(DATABASE_URL)
            connection = engine.connect()
            connection.close()
            print("Database connection successful.")
            break
        except Exception as e:
            print(f"Connection attempt {i+1} failed. Retrying in 5 seconds...")
            time.sleep(5)
    else:
        print("Could not connect to the database after multiple attempts.")
        return

    Session = sessionmaker(bind=engine)
    session = Session()

    print("Dropping and recreating tables...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Tables created.")

    print("Seeding database with sample data...")
    customer1 = Customer(name="Alice Johnson", email="alice@example.com")
    customer2 = Customer(name="Bob Williams", email="bob@example.com")
    product1 = Product(name="Wireless Mouse", price=25.99)
    product2 = Product(name="Mechanical Keyboard", price=89.99)
    order1 = Order(id="A-12345", customer=customer1, product=product1, shipping_address="123 Maple St, Anytown")
    order2 = Order(id="B-54321", customer=customer2, product=product2, shipping_address="456 Oak Ave, Otherville")
    order3 = Order(id="C-98765", customer=customer1, product=product2, shipping_address="123 Maple St, Anytown", status="Shipped")

    session.add_all([customer1, customer2, product1, product2, order1, order2, order3])
    session.commit()
    session.close()
    
    print("✅ Database seeding complete!")

if __name__ == "__main__":
    seed_database()