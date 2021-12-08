'''
Write a function called make_album() that builds dictionary.
The function should take in an artist name and an album title,
it should return a dictionary containing these two informations.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album info correctly.

Use None to add an optional paramater to make_album() that allows you to store the number of songs.
If the calling line includes a value for the number of songs, add that value to the album's dicttionary.
Make at least one new function call that includes the number of songs on an album.
'''


def make_album(aname, atitle, nsong=None):
    '''
        Builds album dictionary
    :param aname: Takes artist name
    :param atitle: Takes album title
    :param nsong: optional, takes number of songs
    :return: Builds dictionary
    '''
    album = {'artist': aname, 'album': atitle, }
    if nsong:
        album['number of songs'] = nsong

    return album


print(make_album('Majke', 'Razdor'))
print(make_album('AC/DC', 'Highway to hell', 12))

print('\n')
help(make_album)

'''
Autorova rjesenja
https://ehmatthes.github.io/pcc_2e/solutions/chapter_8/
'''

#tags: function, dictionary, docstring,