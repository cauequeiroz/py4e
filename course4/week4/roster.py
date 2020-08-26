# This application will read roster data in JSON format, parse the file, and then
# produce an SQLite database that contains a User, Course, and Member table and populate
# the tables from the data file.

import json
import sqlite3

# Database
# --------------------------------------------------------

connection = sqlite3.connect('roster.sqlite')
database = connection.cursor()

database.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
''')

# Read roster_data.json
# --------------------------------------------------------

file_handler = open('roster_data.json')
document = json.load(file_handler)

for user in document:
    (name, course, role) = user
    
    database.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    database.execute('SELECT id FROM User WHERE name=?', (name,))
    user_id = database.fetchone()[0]

    database.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    database.execute('SELECT id FROM Course WHERE title=?', (course,))
    course_id = database.fetchone()[0]

    database.execute(
        'INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',
        (user_id, course_id, role)
    )    

connection.commit()
connection.close()

