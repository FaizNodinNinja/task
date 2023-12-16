import mysql.connector


# Function to create a new database, table, and columns
def create_database_and_table():
    # Connect to MySQL server (you need to provide your own host, user, and password)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faiz1234",
        database = "studentalldata"

    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS studentalldata")

    # Switch to the newly created database
    # cursor.execute("USE students")

    # Create the 'students' table
    cursor.execute("CREATE TABLE IF NOT EXISTS students ("
                   "student_id INT AUTO_INCREMENT PRIMARY KEY, "
                   "first_name VARCHAR(50), "
                   "last_name VARCHAR(50), "
                   "age INT, "
                   "grade FLOAT)"
                   )

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()


# Function to insert a new student record
def insert_student_record():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faiz1234",
        database="studentalldata"
    )
    cursor = connection.cursor()


#
#    # Insert a new student record
    cursor.execute("INSERT INTO students (first_name, last_name, age, grade) "
                   "VALUES (%s, %s, %s, %s)",
                   ("Smith", "Alice", 18, 95.5))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

# Function to update the grade of the student with the first name "Alice"
def update_student_grade():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faiz1234",
        database="studentalldata"
    )
    cursor = connection.cursor()

    # Update the grade of the student with the first name "Alice"
    cursor.execute("UPDATE students SET grade = %s WHERE first_name = %s",
                   (97.0, "Alice"))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()
#
# # Function to delete the student with the last name "Smith"
def delete_student():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faiz1234",
        database="studentalldata"
    )
    cursor = connection.cursor()

    # Delete the student with the last name "Smith"
    cursor.execute("DELETE FROM students WHERE last_name = %s", ("Smith",))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()
#
# # Function to fetch and display all student records
def fetch_and_display_students():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="faiz1234",
        database="studentalldata"
    )
    cursor = connection.cursor()

    # Fetch all student records
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    # Display the fetched records
    for record in records:
        print(record)

    # Close the connection
    cursor.close()
    connection.close()

# Main function to execute the tasks
def main():
    create_database_and_table()
    insert_student_record()
    update_student_grade()
    # delete_student()
    # fetch_and_display_students()


if __name__ == "__main__":
    main()
