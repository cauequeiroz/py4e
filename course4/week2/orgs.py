import sqlite3

# This application will read the mailbox data (mbox.txt) and count the number
# of email messages per organization (i.e. domain name of the email address) using
# a database to maintain the counts.

# create frequency dict based on mbox.txt
# -----------------------------------------------------------------------------

org_count = dict()

file_name = 'mbox.txt'
file_handle = open(file_name, 'r')

for line in file_handle:
    if not line.startswith('From: '): continue

    org = line.rstrip().split('@')[1]
    org_count[org] = org_count.get(org, 0) + 1

file_handle.close()

# saves on database
# -----------------------------------------------------------------------------

connection = sqlite3.connect('emaildb.sqlite')
database = connection.cursor()

database.execute('DROP TABLE IF EXISTS Counts')
database.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

for (org, count) in org_count.items():
    database.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, count))

connection.commit()
connection.close()