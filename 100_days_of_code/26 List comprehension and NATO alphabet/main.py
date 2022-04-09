import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_dataframe = pandas.read_csv('./nato_phonetic_alphabet.csv')
nato_dictionary = {row['letter']: row['code'] for index, row in nato_dataframe.iterrows()}

user_input = input('Enter a word: ')
nato_list = [nato_dictionary[letter] for letter in user_input]
print(nato_list)


#modules: pandas,
#tags: list, dictionary, comprehension, input(), iterrows()
