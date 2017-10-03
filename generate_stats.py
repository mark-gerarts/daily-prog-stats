import sqlite3

# Dict factory used to return SQL results as a dict.
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('daily_prog_stats.db')
conn.row_factory = dict_factory


class Submission(object):
    def __init__(self, **kwargs):
        defaults = {
            'id': None,
            'user': None,
            'body': None,
            'parent_id': None,
            'parent_title': None,
            'created': None,
            'language': None
        }
        for (prop, default) in defaults.items():
            setattr(self, prop, kwargs.get(prop, default))


def result_to_submission(result):
    return Submission(**result) if result else None

def get_next_unparsed_submission():
    c = conn.cursor()
    c.execute('SELECT * FROM submissions WHERE language IS NULL LIMIT 1')
    return result_to_submission(c.fetchone())

def extract_language(body):
    # @todo
    return None
