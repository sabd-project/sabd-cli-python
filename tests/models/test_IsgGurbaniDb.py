#! /usr/bin/python

import unittest
import application.bootstrap
from application.models.IsgGurbaniDb import IsgGurbaniDb


class test_IsgGurbaniDb(unittest.TestCase):
    _object = None

    def setUp(self):
        self._object = IsgGurbaniDb(application.bootstrap.config)

    def test_first_letter_search(self):
        query = 'hjkkqp'  #Har Jeeo Kirapaa Karahu Thum Piaarae
        self.assertEqual(self._object.first_letter_search(query),
                         [(26355, 2289, u'Har Jeeo Kirapaa Karahu Thum Piaarae ||')],
                         "does it return a sabad for a known query")

        query = 'zzzzzzzz1222'
        self.assertEqual(self._object.first_letter_search(query), [], "does it return an empty array for a dodgy query")

        #If No Query passed in
        with self.assertRaises(TypeError):
            self._object.first_letter_search()

    def test_get_sabad_by_sabad_id(self):
        sabad_id = 1283  #sahib kare kabool
        expected_data = [(14760, 323, u'sggs', 7, 1283, u'm\xda 5 ]', u'M\u0117hl\u0101 5.', u'Fifth Mehl:'), (
            14761, 323, u'sggs', 8, 1283, u'jwicku mMgY inq nwmu swihbu kry kbUlu ]',
            u'J\u0101c\u1e96ik mangai ni\u1e6f n\u0101m s\u0101hib kare kab\u016bl.',
            u"If the beggar begs for the Lord's Name every day, his Lord and Master will grant his request."), (
                             14762, 323, u'sggs', 8, 1283, u'nwnk prmysru jjmwnu iqsih BuK n mUil ]2]',
                             u'N\u0101nak parmesar jajm\u0101n \u1e6fis\u0117h b\u1e96uk\u1e96 na m\u016bl. ||2||',
                             u'O Nanak, the Transcendent Lord is the most generous host; He does not lack anything at all. ||2||')]
        self.assertEqual(self._object.get_sabad_by_sabad_id(sabad_id), expected_data,
                         "does it return a sabad for a known sabad_id")
        sabad_id = 0
        self.assertEqual(self._object.get_sabad_by_sabad_id(sabad_id), [],
                         "does it return an empty array for a dodgy sabad_id")

        #If No id passed in
        with self.assertRaises(TypeError):
            self._object.first_letter_search()