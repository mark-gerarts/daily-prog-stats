import csv
import sqlite3

conn = sqlite3.connect('daily_prog_stats.db')

def create_tables():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions
                 (id text PRIMARY KEY,
                  body text,
                  user text,
                  parent_id text,
                  parent_title text,
                  created timestamp)''')
    conn.commit()

def parse_csv(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row
        next(reader)
        for row in reader:
            parse_row(row)
            conn.commit()

def parse_row(row):
    comment_id, body, user, created, parent_id, parent_title = row
    c = conn.cursor()
    c.execute('SELECT id FROM submissions WHERE id = ?', (comment_id,))
    if not c.fetchone():
        c.execute(
            'INSERT INTO submissions VALUES (?,?,?,?,?,?)',
            (comment_id, body, user, parent_id, parent_title, created)
        )
