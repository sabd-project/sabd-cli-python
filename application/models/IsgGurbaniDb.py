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
        query = "select ID,shabd,roman from gurbani where gamma like ? order by ID,page,line"
        cursor.execute(query, [input + '%'])
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_sabad_by_sabad_id(self, sabad_id):
        """
        get a specific sabad by sabad_id
        @param int the sabad id
        @return the data
        """

        if sabad_id == None:
            raise TypeError('no sabad_id passed in')

        cursor = self._connection.cursor()
        query = "select ID,page,scrpt,line,shabd,gurmukhi,translit,english from gurbani where shabd=? order by ID,page,line"
        cursor.execute(query, [sabad_id])
        data = cursor.fetchall()
        cursor.close()

        return data