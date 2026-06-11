import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import random
import pandas as pd
from faker import Faker

from config.db_config import get_engine

# --------------------------------------------------
# Configuration
# --------------------------------------------------

NUM_CUSTOMERS = 5000
NUM_PRODUCTS = 1000
NUM_ORDERS = 50000

fake = Faker("en_IN")
engine = get_engine()

# --------------------------------------------------
# Customers
# --------------------------------------------------

print("Generating customers...")

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad"
]

customers = []

for _ in range(NUM_CUSTOMERS):
    customers.append(
        {
            "customer_name": fake.name(),
            "city": random.choice(cities),
            "signup_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        }
    )

customers_df = pd.DataFrame(customers)

customers_df.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=1000
)

print(f"✅ {NUM_CUSTOMERS} customers loaded")

# --------------------------------------------------
# Products
# --------------------------------------------------

print("Generating products...")

categories = [
    "Electronics",
    "Fashion",
    "Books",
    "Furniture",
    "Grocery",
    "Sports",
    "Beauty"
]

products = []

for _ in range(NUM_PRODUCTS):
    products.append(
        {
            "product_name": fake.word().title(),
            "category": random.choice(categories),
            "price": round(
                random.uniform(100, 50000),
                2
            )
        }
    )

products_df = pd.DataFrame(products)

products_df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=1000
)

print(f"✅ {NUM_PRODUCTS} products loaded")

# --------------------------------------------------
# Orders
# --------------------------------------------------

print("Generating orders...")

orders = []

for _ in range(NUM_ORDERS):

    customer_id = random.randint(1, NUM_CUSTOMERS)

    product_id = random.randint(1, NUM_PRODUCTS)

    amount = round(
        random.uniform(100, 25000),
        2
    )

    orders.append(
        {
            "customer_id": customer_id,
            "product_id": product_id,
            "amount": amount,
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        }
    )

orders_df = pd.DataFrame(orders)

orders_df.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=5000
)

print(f"✅ {NUM_ORDERS} orders loaded")

# --------------------------------------------------
# Payments
# --------------------------------------------------

print("Generating payments...")

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet"
]

payment_statuses = [
    "Success",
    "Failed",
    "Pending"
]

payments = []

for order_id in range(1, NUM_ORDERS + 1):

    payments.append(
        {
            "order_id": order_id,
            "payment_method": random.choice(
                payment_methods
            ),
            "payment_status": random.choice(
                payment_statuses
            )
        }
    )

payments_df = pd.DataFrame(payments)

payments_df.to_sql(
    "payments",
    engine,
    if_exists="append",
    index=False,
    method="multi",
    chunksize=5000
)

print(f"✅ {NUM_ORDERS} payments loaded")

print("\n🎉 Data loading completed successfully!")