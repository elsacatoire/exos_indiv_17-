import unittest
from main import cut_text, reconstruction_sentence


class PhraseUtilsTests(unittest.TestCase):
    def test_cut_text(self):
        # Test case 1
        sentence_to_cut = "Hello, how are you ?"
        result = cut_text(sentence_to_cut)
        expected = ["Hello,", "how", "are", "you", "?"]
        self.assertEqual(result, expected)

        # Test case 2
        sentence_to_cut = "J'aime les chiens et les chats"
        result = cut_text(sentence_to_cut)
        expected = ["J'aime", "les", "chiens", "et", "les", "chats"]
        self.assertEqual(result, expected)

    def test_reconstruction_sentence(self):
        # Test case 1
        mots = ["Hello,", "how", "are", "you", "?"]
        result = reconstruction_sentence(mots)
        expected = "Hello, how are you ?"
        self.assertEqual(result, expected)

        # Test case 2
        mots = ["J'aime", "les", "chiens", "et", "les", "chats"]
        result = reconstruction_sentence(mots)
        expected = "J'aime les chiens et les chats"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

