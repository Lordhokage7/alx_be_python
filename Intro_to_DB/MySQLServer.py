import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (no specific database yet)
        connection = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="root"  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        # Close the connection safely
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # You can print confirmation (optional)
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
