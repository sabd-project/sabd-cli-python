import sqlite3
import os.path


class IsgGurbaniDb:
    '''
    to model the http://searchgurbani.com/sgdv/isg sqllite db
    '''
    _config = None
    _connection = None

    def __init__(self, config):
        if config == None:
            raise TypeError('config not passed in')

        self._config = config

        # don't try catch as we actually want to throw if there's an issue
        db_path = os.path.join(self._config.get('production', 'APPLICATION_PATH'),
                               self._config.get('production', 'db.isg.path'))

        self._connection = sqlite3.connect(db_path)


    def first_letter_search(self, input):
        """
        First letter search using the gamma field
        @param string the first letter search query
        @return the data
        """

        if input == None:
            raise TypeError('no search string passed in')

        cursor = self._connection.cursor()
        query = "select ID,roman from gurbani where gamma like ?"
        cursor.execute(query, [input + '%'])
        data = cursor.fetchall()
        return data
