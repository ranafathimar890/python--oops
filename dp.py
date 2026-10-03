
import sqlite3


# ddl command(create,alter)


# Create/connect to database
conn = sqlite3.connect("tution.db")

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth DATE,
        age INT,
        genter TEXT,
        mobile_number INT,
        email_address TEXT,
        password TEXT,
        preferred_language TEXT,
        school_college_name TEXT,
        class_grade TEXT,
        board_curriculam TEXT,
        academic_year INT,
        subjects TEXT,
        current_level TEXT,
        areas_topic_help TEXT
    );
    """
)


# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")
