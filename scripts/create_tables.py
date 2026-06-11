from sqlalchemy import text

from config.db_config import get_engine

engine = get_engine()

ddl = """

CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    signup_date DATE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id INTEGER REFERENCES products(product_id),
    amount NUMERIC(10,2),
    order_date DATE
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS query_logs (
    query_id SERIAL PRIMARY KEY,
    user_query TEXT,
    generated_sql TEXT,
    execution_time FLOAT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""

with engine.connect() as conn:
    conn.execute(text(ddl))
    conn.commit()

print("✅ Tables created successfully")