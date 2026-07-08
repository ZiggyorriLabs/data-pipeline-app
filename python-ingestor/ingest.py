import os
import psycopg2
from datetime import datetime

# Grab database connection details from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "portfolio_data")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def run_ingestion():
    print(f"Connecting to database at {DB_HOST}...")
    
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()

    # Create a simple logs table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingestion_logs (
            id SERIAL PRIMARY KEY,
            runtime TIMESTAMP NOT NULL,
            status VARCHAR(50) NOT NULL
        );
    """)
    
    # Insert a new execution log
    current_time = datetime.now()
    cursor.execute(
        "INSERT INTO ingestion_logs (runtime, status) VALUES (%s, %s);",
        (current_time, "SUCCESS")
    )
    
    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"Successfully logged ingestion runtime at {current_time}")

if __name__ == "__main__":
    run_ingestion()