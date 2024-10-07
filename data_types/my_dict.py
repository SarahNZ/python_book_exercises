my_dict = {
    'title': 'Throne of Glass',
    'characters': [
        'Dorian',
        'Aelin',
        'Mannon'
    ],
    'author': 'Sarah J Mass',
    'first published': 2012,
}

my_dict['first published'] = 2013
del my_dict['first published']
print(my_dict)