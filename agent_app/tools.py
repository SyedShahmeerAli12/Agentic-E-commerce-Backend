# agent_app/tools.py (Resilient Version)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .models import Order, Customer

DATABASE_URL = "postgresql://katalyst:12345@postgres-db:5432/katalystdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_order_status(order_id: str) -> dict:
    """Retrieves the status and shipping address for a given order ID."""
    with get_db() as db:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return {"status": "error", "error_message": f"Order '{order_id}' not found."}
        report = f"Order {order.id} status is '{order.status}', shipping to '{order.shipping_address}'."
        return {"status": "success", "report": report}

def find_orders_by_customer(customer_email: str) -> dict:
    """Finds all order IDs for a given customer's email."""
    with get_db() as db:
        customer = db.query(Customer).filter(Customer.email == customer_email).first()
        if not customer or not customer.orders:
            return {"status": "error", "error_message": f"No orders found for '{customer_email}'."}
        order_ids = [order.id for order in customer.orders]
        report = f"Found orders for {customer_email}: {', '.join(order_ids)}."
        return {"status": "success", "report": report}

def cancel_order(order_id: str) -> dict:
    """Cancels an order if its status is 'Pending'."""
    with get_db() as db:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            return {"status": "error", "error_message": f"Order '{order_id}' not found."}
        if order.status != "Pending":
            report = f"Order {order.id} cannot be cancelled (Status: '{order.status}')."
            return {"status": "error", "error_message": report}
        order.status = "Cancelled"
        db.commit()
        return {"status": "success", "report": f"Successfully cancelled order {order.id}."}