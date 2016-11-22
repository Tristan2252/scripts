
def translate_word(word):
    """
    takes in a word and tests for vowels in the first letter, if
    a vowel is found then 'way' is added to it else the letters
    before a vowel are added to the end with 'ay' following it.
    :param word: str # word to translate
    :return: stt # translated word
    """
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels:
        return word + "way"
    else:
        for num, letter in enumerate(word):
            if letter in vowels:
                return word[num:] + word[:num] + "ay"


def openfile(filename):
    """
    takes in file name and attempts to open the files, if the file
    is not found then 'file not found' error is presented to user.
    :param filename: str # name of the file
    :return: [] # list of file contents
    """
    try:
        with open(filename) as fil:
            words = fil.read()
            word_list = words.split()
            return word_list
    except FileExistsError:
        print("\n === File not found ===\n")


def translate_sen(sentence):
    """
    takes in a list of words representing a sentence and passes them
    on to the translate word function to translate the sentence.
    :param sentence: [] # list of words
    :return: str # translated sentence
    """
    translated = []
    for word in sentence:
        translated.append(translate_word(word))

    return " ".join(translated)


def piglatin():
    file_lst = openfile("test.txt")
    word_lst = []
    for word in file_lst:
        word_lst.append(word)

    print("\n" + translate_sen(word_lst) + "\n")

if __name__ == '__main__':
    piglatin()