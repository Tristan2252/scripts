import random


def open_file(file_name):
    with open(file_name) as fl:
        contents = fl.read()
        word_lst = contents.split()
        return word_lst


def make_dict(words):
    dictionary = {}
    for word in words:
        dictionary[word] = []

    return dictionary


def get_words(words, word_dict):
    for i, word in enumerate(words):
        if i == len(words) - 1:
            break
        else:
            lst = word_dict[word]
            lst.append(words[i + 1])

    return word_dict


def start_chain(words):
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    while True:
        choose_word = random.choice(words)
        if choose_word[0] in caps:
            return choose_word


def add_chain(word, word_dict):
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
    cnt = 0
    while True:
        choose_word = random.choice(word_dict[word])
        if choose_word[0] not in caps:
            return choose_word
        elif cnt > 10:
            return "."
        cnt += 1


def markov2():
    words = open_file("test.txt")
    word_dict = make_dict(words)
    markov_dict = get_words(words, word_dict)
    starting_word = start_chain(words)

    punctuation = [".", "!", "?", ")", "\n", ","]
    markov_str = []
    temp_word = starting_word
    while True:
        add_word = add_chain(temp_word, markov_dict)
        if add_word[-1] in punctuation:
            markov_str.append(add_word)
            break
        elif add_word[-1] not in punctuation:
            markov_str.append(add_word)
            temp_word = add_word
        else:
            break
    print(markov_str)
    print("\n{} {}".format(starting_word, " ".join(markov_str)))


if __name__ == '__main__':
    markov2()