import psycopg2

try:
    conn = psycopg2.connect(
        host="database-1.cu9om4g0scai.us-east-1.rds.amazonaws.com",
        port=5432,
        database="postgres",
        user="nl2sqldb",
        password="Dd992613"
    )

    print("✅ Connected Successfully!")

    conn.close()

except Exception as e:
    print("❌ Error:")
    print(e)