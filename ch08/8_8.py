def make_album(artistname, album_title, num_songs=None):
    if not num_songs:
        person = {'artist':artistname, 'album':album_title}
    else:
        person = {'artist':artistname, 'album':album_title, 'number_of_songs':num_songs}
    return person

done = False

albums = []
while not done:
    name = input("artist name: ")
    album = input("album name: ")
    albums.append(make_album(name, album))
    more = input("More album? ")
    if more == 'no':
        done = True

for musician in albums:
    print(f"name: {musician['artist']}, album_name: {musician['album']}")
    



