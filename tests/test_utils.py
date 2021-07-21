import unittest

from src import utils


class GetVocab(unittest.TestCase):
    def test_get_vocab(self):
        result = utils.get_vocab()
        self.assertIsNotNone(result)


class TestCreateCharsToWordsMap(unittest.TestCase):
    def test_create_chars_to_words_map(self):
        result = utils.create_chars_to_words_map(['read', 'dear'])
        self.assertEqual(result, {'ader': ['read', 'dear']})


class GetWordsFromChars(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chars_to_words_map = utils.create_chars_to_words_map(['read', 'dear'])

    def test_get_words_from_chars_len(self):
        text = 'read'
        result = utils.get_words_from_chars(text, self.chars_to_words_map)
        self.assertEqual(len(result), 2)

    def test_get_words_from_chars(self):
        text = 'read'
        result = utils.get_words_from_chars(text, self.chars_to_words_map)
        self.assertEqual(result, ['read', 'dear'])

    def test_get_words_from_chars_single(self):
        text = 'a'
        result = utils.get_words_from_chars(text, self.chars_to_words_map)
        self.assertEqual(result, ['a'])

    def test_get_words_from_chars_empty(self):
        text = ''
        result = utils.get_words_from_chars(text, self.chars_to_words_map)
        self.assertEqual(result, [''])


class TestGetPermutations(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chars_to_words_map = utils.create_chars_to_words_map(['read', 'dear'])

    def test_get_permutations_len(self):
        text = 'read dear'
        result = utils.get_permutations(text, self.chars_to_words_map)
        self.assertEqual(len(result), 4)

    def test_get_permutations(self):
        text = 'read'
        result = utils.get_permutations(text, self.chars_to_words_map)
        self.assertEqual(result, [('read',), ('dear',)])


class ScrambleWords(unittest.TestCase):
    def test_scramble_words(self):
        text = 'this is a test'
        result = utils.scramble_words(text)
        self.assertNotEqual(result, text)
