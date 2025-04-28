def make_album(artistname, album_title, num_songs=None):
    if not num_songs:
        person = {'artist':artistname, 'album':album_title}
    else:
        person = {'artist':artistname, 'album':album_title, 'number_of_songs':num_songs}
    return person

musician1 = make_album('hassan','bauler ektara')
musician2 = make_album('prohori','moruvumi')
musician3 = make_album('james','lace fita')
musician4 = make_album('james','lace fita', 12)

musicians = [musician1, musician2, musician3,musician4]
for musician in musicians:
    if 'number_of_songs' in musician:
        print(f"name: {musician['artist']}, album_name: {musician['album']}, number: {musician['number_of_songs']}")
    else:
        print(f"name: {musician['artist']}, album_name: {musician['album']}")
    


