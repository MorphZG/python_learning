# Hint1: file.readlines()
# Hint2: string.replace(old, new, count)
# Hint3: string.strip(characters)

names_path = "./Input/Names/invited_names.txt"
letter_path = "./Input/Letters/starting_letter.txt"

# read names and store in variable
with open(names_path) as fnames:
    names_content = fnames.readlines()  # readlines() returns list of lines
    # names_content belongs to global space

# read the whole letter as single string
with open(letter_path) as fletter:
    letter_content = fletter.read()

# strip whitespace and replace [name] in starting letter
for name in names_content:
    clean_name = name.strip()
    final_output = letter_content.replace("[name]", clean_name)

    # write new file for every name
    with open(f"./Output/ReadyToSend/letter_{clean_name}.txt", mode="w") as new_file:
        new_file.write(final_output)
        print(f"letter for {clean_name} written!")

print("\nWork complete!")

# I have intreset in regular expressions for a long time. That is also one
# of reasons why i use grep and tag these python files. Would be good practice
# build the same program using builtin "re" module for regular expressions.

print("Now try the regex version")

#tags: files, i/o stream, regex, automation
