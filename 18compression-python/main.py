

def cut_text(text_to_cut):
    result = text_to_cut.split(' ')
    return result


def reconstruction_sentence(words):
    result = " ".join(words)
    return result


def replace_some_words(words_to_check, swapping_words):
    for i in range(len(words_to_check)):
        for key in swapping_words.keys():
            if words_to_check[i] == key:
                words_to_check[i] = swapping_words[key]
    return words_to_check


def compress_words(text_to_compress):
    compression_dictionary = {'texte': '1', 'lorem': '2', 'qui': '3', 'donc': '4',
                              'est': '5', 'que': '6', 'pour': '7', 'ceci': '8',
                              'faux-texte': '9', 'dans': '10', 'plus': '11', 'avec': '12'}
    words_list = cut_text(text_to_compress)
    compression_list = replace_some_words(words_list, compression_dictionary)
    compressed_sentence = reconstruction_sentence(compression_list)
    return compressed_sentence


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_list = replace_some_words(["chat", "rat", "lion", "hello"], {"chat": "1", "quoi": "2", "lion": "12"})
    print(new_list)
    yo = compress_words('mais ceci est un long faux-texte')
    print(yo)
