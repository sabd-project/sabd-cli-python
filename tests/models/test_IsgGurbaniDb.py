#! /usr/bin/python

import unittest
import application.bootstrap
from  application.models.IsgGurbaniDb import IsgGurbaniDb


class test_IsgGurbaniDb(unittest.TestCase):
    _object = None

    def setUp(self):
        self._object = IsgGurbaniDb(application.bootstrap.config)

    def test_first_letter_search(self):
        query = 'hjkkqp'
        self.assertEqual(self._object.first_letter_search(query), [(26355, u'Har Jeeo Kirapaa Karahu Thum Piaarae ||')],
                         "does it return a sabad for a known query")

        query = 'zzzzzzzz1222'
        self.assertEqual(self._object.first_letter_search(query), [], "does it return an empty array for a dodgy query")

        #If No Query passed in
        with self.assertRaises(TypeError):
            self._object.first_letter_search()
