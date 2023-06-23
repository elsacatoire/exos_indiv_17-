import random
import itertools


def hello(name):
    print(f"hello {name}")


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello("elsa")
    to_cut = "qu'elle est... » ). expert en utilisabilité des"
    to_join = ["qu'elle", "est...", "»", ").", "expert", "en", "utilisabilité", "des"]
    cut = cut_text(to_cut)
    uncut = reconstruction_sentence(to_join)
    print(cut)
    print(uncut)
    if uncut == to_cut:
        print("oh yeah")

    new_list = replace_some_words(["chat", "rat", "lion", "hello"], {"chat": "1", "quoi": "2", "lion": "12"})
    print(new_list)