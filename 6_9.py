favorite_places = {
    'rony': ['rangamati', 'chalanbil','tsc'],
    'humayun': ['shahid minar', 'khagrachori','bandarban'],
    '': ['rangamati', 'chalanbil','tsc'],
}

for name, place in favorite_places.items():
    print(f"{name}'s favorite places are: {', '.join(place)}")