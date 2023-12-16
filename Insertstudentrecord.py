import mysql.connector

# Function to create a new database, table, and columns
# Connect to MySQL server (you need to provide your own host, user, and password)
mydb = mysql.connector.connect(host='localhost', user='root', password='faiz1234', database='studentrecord')
cur = mydb.cursor()

# Create a cursor object to execute SQL queries

# Create the database---------
cur.execute("CREATE DATABASE studentrecord")


# ------------ Create the 'student' table
cur = mydb.cursor()
student=("CREATE TABLE student("
         "student_id INT AUTO_INCREMENT PRIMARY KEY, "
         "first_name VARCHAR(50),"
         "last_name VARCHAR(50), age INT, "
         "grade FLOAT)")
cur.execute(student)


# --------------Insert a data in a table -----------
mydb.cursor()
student = "INSERT INTO student (student_id,first_name,last_name,age,grade) VALUE (%s, %s, %s, %s, %s)"
data = [(1, 'Alice', 'Smith', 18, 94.8),(2, 'Smith', 'Alice', 18, 94.8), (3, 'faiz', 'ali', 18, 96.8)]
cur.executemany(student, data)
mydb.commit()


# Function to fetch and display all student records----------
mydb.cursor()
student = "select * from student"
cur.execute(student)
result = cur.fetchall()
for rec in result:
    print(rec)


# ---------- Function to update the grade of the student with the first name "Alice"-------------
cur = mydb.cursor()
student = "UPDATE student SET grade = 97.0 WHERE first_name = 'Alice'"
cur.execute(student)
mydb.commit()



# ----------Function to fetch and display all student records----------
mydb.cursor()
student = "select * from student"
cur.execute(student)
result = cur.fetchall()
for rec in result:
    print(rec)


# -----------Function to delete the student with the last name "Smith"---------
cur = mydb.cursor()
student = "DELETE FROM student WHERE last_name = 'Smith' "
cur.execute(student)
mydb.commit()


# ----------Function to fetch and display all student records----------
mydb.cursor()
student = "select * from student"
cur.execute(student)
result = cur.fetchall()
for rec in result:
    print(rec)

