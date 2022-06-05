# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
print(phonetic_dict)


def generate_phonetic_word():
    """ generates phonetic word from the NATO alphabet """
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic_word()
    else:
        print(output_list)


generate_phonetic_word()


#modules: pandas
#tags: error, exception, recursion, function, iterrows()
