'''
Start with your porogram from 8-7.
Write a while loop that allows users to enter an album's artist and title.
Once you have that information call make_album() with the users input
and print the dictionary thats created.
Be sure to include a quit value in the while loop.
'''

# <! --- definicija funkcije
def make_album(aname, atitle, nsong=None):
    ''' Builds album dictionary '''
    album = {'artist': aname.title(), 'album': atitle.title(), }
    if nsong:
        album['number of songs'] = nsong

    return album

# <! --- input prompt
aname_prompt = 'Type the artist name:\n>'
atitle_prompt = 'Type the album title:\n>'
nsong_prompt = 'How many songs there is:\n>'

# <! --- while loop, user input
while True:
    aname = input(aname_prompt)
    atitle = input(atitle_prompt)
    nsong = input(nsong_prompt)
    quit = input('type "q" to print or "c" to continue')
    if quit == 'q':
        break
    elif quit == 'c':
        continue  # continue statement goes back to start
                  # pass statement does nothing and moves to next line 

# <! --- call function and print
print(make_album(aname, atitle, nsong))


'''
Autorova rjesenja
https://ehmatthes.github.io/pcc_2e/solutions/chapter_8/
'''

def make_album(artist, title, tracks=0):
    """ Builds album dictionary """
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")


#tags: function, while loop, input(), dictionary,