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

database.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    );

    CREATE TABLE Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER
    );
''')

# Start application
# --------------------------------------------------------

tracks = get_content('Library.xml')

for track in tracks:
    # Handle artist
    database.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (track.get('artist'),))
    database.execute('SELECT id FROM Artist WHERE name=?', (track.get('artist'),))
    artist_id = database.fetchone()[0]

    # Handle genre
    database.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (track.get('genre'),))
    database.execute('SELECT id FROM Genre WHERE name=?', (track.get('genre'),))
    genre_id = database.fetchone()[0]

    # Handle album
    database.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (track.get('album'), artist_id))
    database.execute('SELECT * FROM Album WHERE title=?', (track.get('album'),))
    album_id = database.fetchone()[0]

    # Handle track
    database.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id) VALUES (?, ?, ?)', (track.get('name'), album_id, genre_id))

connection.commit()
connection.close()