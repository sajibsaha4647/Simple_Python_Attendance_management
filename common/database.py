from django.db import connection, DatabaseError


def check_database_connection():
    try:
        connection.ensure_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1") 
            cursor.fetchone()

        print("✅ PostgreSQL connected successfully!")
        return True

    except DatabaseError as error:
        print("❌ PostgreSQL connection failed:", error)
        return False