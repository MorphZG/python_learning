'''User Profile
Start with a copy of user_profile.py from page 149.
Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs
'''


# <! --- ovo je definicija iz knjige, autor vec u 8-14 koristi bolji format
def build_profile(first, last, **user_info):
    ''' build a dictionary containing everything we know about user. '''
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info
# < --- kraj


user_profile = build_profile(
    'zoran', 'topic',
    location='zagreb',
    field='programing',
    language='python')

print(user_profile)


# <! --- ovakva definicija mi je puno logicnija
def izgradi_profil(ime, prezime, **kwargs):
    # gradim klasican dictionary za poznate parametre(ime i prezime)
    profil = {
    'ime': ime,
    'prezime': prezime,
    }

    # obzirom da neznam koliko ce biti ostalih itema
    # njih odredujem kao **kwargs
    # radim for loop koji ce popuniti prethodno definirani dictionary
    for k, v in kwargs.items():
        profil[k] = v
    return profil


user_profile2 = izgradi_profil(
    'zoran', 'topic',
    location='zagreb',
    field='programing',
    language='python')

print(user_profile2)

# single asterix * represents optional number of positional arguments
# while double asterix ** represents optional number of keyword arguments
# when writing def block, both must be placed after all other parameters

#tags: function, dictionary, arg, kwarg