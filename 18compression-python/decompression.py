
from compression import cut_text, reconstruction_sentence


def decode_words(code, swapping_dictionary):
    inverted_dictionary = {v: k for k, v in swapping_dictionary.items()}
    for i in range(len(code)):
        if code[i] in inverted_dictionary:
            code[i] = inverted_dictionary[code[i]]
    return code


def text_reconstruction(to_decode):
    dictionary = {'texte': '1', 'lorem': '2', 'qui': '3', 'donc': '4',
                              'est': '5', 'que': '6', 'pour': '7', 'ceci': '8',
                              'faux-texte': '9', 'dans': '10', 'plus': '11', 'avec': '12'}
    to_decode_list = cut_text(to_decode)
    decompressed_list = decode_words(to_decode_list, dictionary)
    decompressed_sentence = reconstruction_sentence(decompressed_list)
    return decompressed_sentence


text_reconstruction('mais 8 5 un long 9')


