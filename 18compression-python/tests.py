import unittest
from main import cut_text, reconstruction_sentence


class PhraseUtilsTests(unittest.TestCase):
    def test_cut_text(self):
        # Test case 1
        sentence_to_cut = "Bonjour, comment ça va ?"
        result = cut_text(sentence_to_cut)
        expected = ["Bonjour,", "comment", "ça", "va", "?"]
        self.assertEqual(result, expected)

        # Test case 2
        sentence_to_cut = "J'aime les chiens et les chats."
        result = cut_text(sentence_to_cut)
        expected = ["J'aime", "les", "chiens", "et", "les", "chats", "."]
        self.assertEqual(result, expected)

