# use prettytable documentation and build an ASCII table with
# two columns, first will hold a list of pokemon names and second
# will hold type of those pokemons.

# https://pypi.org/project/prettytable/

from prettytable import PrettyTable

# create instance of PrettyTable()
table = PrettyTable()

# create fields and rows
table.field_names = ['Pokemon name', 'type']
table.add_rows([

    ['Pikachu', 'Electric'],
    ['Squirtle', 'Water'],
    ['Charmander', 'Fire']
])

# align the text left
table.align = 'l'
print(table)


#modules: prettytable
#tags: ASCII