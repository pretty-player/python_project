import sqlite3

def manage_students():
    db_file = 'school_data.db'
    conn = None
    
    try:
        # 1. Connect to SQLite (Creates the file if it doesn't exist)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT,
                age INTEGER
            )
        """)

        # --- TRANSACTION START ---
        # 2. CREATE (Insert)
        students_to_add = [
            ("Alice", "A", 20),
            ("Bob", "B", 22),
            ("Charlie", "C", 21)
        ]
        cursor.executemany("INSERT INTO students (name, grade, age) VALUES (?, ?, ?)", students_to_add)

        # 3. UPDATE
        cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Bob"))

        # 4. DELETE
        cursor.execute("DELETE FROM students WHERE name = ?", ("Charlie",))

        # Commit changes
        conn.commit()
        print("Successfully performed CRUD operations and committed changes.")

    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # 5. READ (Fetch and Display)
        if conn:
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            
            print("\n--- Current Student Records ---")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]} | Age: {row[3]}")
            
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    manage_students()