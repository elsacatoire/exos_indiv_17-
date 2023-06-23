
# methods to compress a text :
def cut_text(text_to_cut):
    """
    cuts a any string
    :param text_to_cut: the text yu need to cut
    :return: an array with all the words in the text
    """
    result = text_to_cut.split(' ')
    return result


def reconstruction_sentence(words):
    """
    takes any array and make it a sentence
    :param words: a list of words o characters
    :return: a text, string
    """
    result = " ".join(words)
    return result


def replace_some_words(words_to_check, swapping_words):
    """
    allows us to swap some elements from a list using a dictionary
    :param words_to_check: a list of words
    :param swapping_words: a dictionary of words we want to swap with
    :return: a new list
    """
    for i in range(len(words_to_check)):
        for key in swapping_words.keys():
            if words_to_check[i] == key:
                words_to_check[i] = swapping_words[key]
    return words_to_check


def compress_words(text_to_compress):
    """
    this function uses different methods to compress a piece of text
    :param text_to_compress: give ma piece of text you need to compress
    :return: return a text as a string
    """
    compression_dictionary = {'texte': '1', 'lorem': '2', 'qui': '3', 'donc': '4',
                              'est': '5', 'que': '6', 'pour': '7', 'ceci': '8',
                              'faux-texte': '9', 'dans': '10', 'plus': '11', 'avec': '12'}
    words_list = cut_text(text_to_compress)
    compression_list = replace_some_words(words_list, compression_dictionary)
    compressed_sentence = reconstruction_sentence(compression_list)
    return compressed_sentence
