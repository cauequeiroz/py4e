# This application will read an iTunes export file in XML and produce a properly normalized database

import xml.etree.ElementTree as ET
import sqlite3

# Parse xml
# --------------------------------------------------------

def get_item_content(items, label):
    found = False

    for item in items:
        if item.text == label:
            found = True
        elif found:
            return item.text

def get_content(file):
    tracks_xml = ET.parse(file).findall('dict/dict/dict')
    tracks = list()

    for track in tracks_xml:
        name = get_item_content(track, 'Name')
        artist = get_item_content(track, 'Artist')
        album = get_item_content(track, 'Album')
        genre = get_item_content(track, 'Genre')

        if artist is None or album is None or genre is None:
            continue
        
        track = dict()
        track['name'] = name
        track['artist'] = artist
        track['album'] = album
        track['genre'] = genre

        tracks.append(track)
    
    return tracks

# Database
# --------------------------------------------------------

connection = sqlite3.connect('tracks.sqlite')
database = connection.cursor()

database.execute('DROP TABLE IF EXISTS Artist')
database.execute('DROP TABLE IF EXISTS Genre')
database.execute('DROP TABLE IF EXISTS Album')
database.execute('DROP TABLE IF EXISTS Track')

database.execute('''
    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
''')

database.execute('''
    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
''')

database.execute('''
    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );
''')

database.execute('''
    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT,
        album_id INTEGER,
        genre_id INTEGER
    );
''')

# Start application
# --------------------------------------------------------

tracks = get_content('Library.xml')

for track in tracks:
    # Handle artist
    database.execute('SELECT * FROM Artist WHERE name="'+track.get('artist')+'"')
    artist = database.fetchone()

    if artist is None:
        database.execute('INSERT INTO Artist (name) VALUES (?)', (track.get('artist'),))
        artist_id = database.lastrowid
    else:
        artist_id = artist[0]

    # Handle genre
    database.execute('SELECT * FROM Genre WHERE name="'+track.get('genre')+'"')
    genre = database.fetchone()

    if genre is None:
        database.execute('INSERT INTO Genre (name) VALUES (?)', (track.get('genre'),))
        genre_id = database.lastrowid
    else:
        genre_id = genre[0]

    # Handle album
    database.execute('SELECT * FROM Album WHERE title="'+track.get('album')+'"')
    album = database.fetchone()

    if album is None:
        database.execute('INSERT INTO Album (title, artist_id) VALUES (?, ?)', (track.get('album'), artist_id))
        album_id = database.lastrowid
    else:
        album_id = album[0]

    # Handle track
    database.execute(
        'INSERT INTO Track (title, album_id, genre_id) VALUES (?, ?, ?)',
        (track.get('name'), album_id, genre_id)
    )

connection.commit()
connection.close()