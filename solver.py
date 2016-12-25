def get_possible_words(letters, length):
    """
    This function takes a bunch of letters and returns a list of
    words of a specific length that can be made from those letters

    :param letters: a list of letters (list[])
    :param length: the length of the word that needs to be made (int)
    :return: list[]

    >>> get_possible_words(['h','e','l','l','o'], 5)
    ['hello']

    """
    possible_words = []

    # get a list of dictionary words
    word_file = open("english_words.txt", 'r')
    word_list = get_dict_words(word_file)

    for word in word_list:
        # check if the word is of the appropriate length
        if len(word) == length:

            # check if the word can be created with the given letters
            if is_word_possible(letters, word):
                possible_words.append(word)

    return possible_words


def is_word_possible(letters, word):
    """
    This program takes a list of letters and a word. It then checks if that word can be
     created from the list of letters.

    :param letters: a list of letters (list[])
    :param word: the length of the word that needs to be made (int)
    :return: true or false

    >>> is_word_possible(['h','e','l','l','o'], "hello")
    True
    >>> is_word_possible([], "no")
    False

    """
    # make a clone of the word list
    temp_letters = letters[:]
    for char in word:
        # keep removing instances of letters
        if char in temp_letters:
            temp_letters.remove(char)
        else:
            return False

    return True


def get_dict_words(file):
    """
    This function takes a file containing all english words
     and it returns a list with all those words in it.

    :param file: dictionary file
    :return: list[]
    """
    word_list = []

    for word in file:
        word = word.replace("\n", "")
        word_list.append(word)

    return word_list

# testing
# # get a list of dictionary words
# word_file = open("english_words.txt", 'r')
# word_list = get_dict_words(word_file)
#
# print(word_list)

while True:
    letters = list(str(input("Please input the words given to you from 4PicsOneWord:")))
    length = int(input("How long should the word be?:"))

    possible_words = get_possible_words(letters, length)

    print("\n")
    for word in possible_words:
        print(word)

    print("\n")

    print("We found " + str(len(possible_words)) + " word(s)!")

    is_done = input("Are you done?(y/n)")

    if is_done == "y":
        break
    else:
        pass
    print("\n")




