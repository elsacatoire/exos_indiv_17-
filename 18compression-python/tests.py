import unittest
from main import cut_text, reconstruction_sentence, replace_some_words


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

    def test_replace_some_words(self):
        # Test case 1
        words_to_swap = ['mais', 'ceci', 'est', 'un', 'long', 'faux-texte']
        dictionary = {'texte': '1', 'lorem': '2', 'qui': '3', 'donc': '4', 'est': '5', 'que': '6', 'pour': '7', 'ceci': '8', 'faux-texte': '9', 'dans': '10', 'plus': '11', 'avec': '12'}
        result = replace_some_words(words_to_swap, dictionary)
        expected = ['mais', '8', '5', 'un', 'long', '9']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
