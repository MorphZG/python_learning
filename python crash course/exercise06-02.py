# Use a dictionary to store peoples favorite numbers.
# Take 5 names and use them as keys in dictionary.
# Think of favorite number for each person and store each as a value.
# Print each persons name and their favorite number.
# For even more fun poll a few of your friends and get some actual data

favnumbers = {
    'borna': 19,
    'jelena': 6,
    'zoran': 7,
    'tomislav': 44,
    'bruno': 28
}


for key, value in favnumbers.items():
    print(key, value, sep=":")
