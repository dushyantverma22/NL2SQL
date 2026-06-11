import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sqlalchemy import text
from config.db_config import get_engine

engine = get_engine()

indexes = [

    # Orders Table
    """
    CREATE INDEX IF NOT EXISTS idx_orders_customer
    ON orders(customer_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_orders_product
    ON orders(product_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_orders_date
    ON orders(order_date);
    """,

    # Customers Table
    """
    CREATE INDEX IF NOT EXISTS idx_customers_city
    ON customers(city);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_customers_signup
    ON customers(signup_date);
    """,

    # Products Table
    """
    CREATE INDEX IF NOT EXISTS idx_products_category
    ON products(category);
    """,

    # Payments Table
    """
    CREATE INDEX IF NOT EXISTS idx_payments_status
    ON payments(payment_status);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_payments_method
    ON payments(payment_method);
    """
]

with engine.begin() as conn:

    for index_query in indexes:
        conn.execute(text(index_query))

print("✅ All indexes created successfully!")