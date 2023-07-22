def make_album(artist, title, number_songs=None):
    """Make an album with the artist name, title of the album and
    number of songs(optional)"""
    album = {
        'artist': artist.title(),
        'title': title.title(),
    }

    if number_songs:
        album['num_songs'] = number_songs

    return album


print("This is a program to make albums")
print("Please enter 'q' anytime to quit.")

while True:
    artist = input("\nEnter the artist name: ")
    if artist == 'q':
        break

    title = input("\nEnter the title of the album: ")
    if title == 'q':
        break

    songs = input("\nHow many songs does it have (optional): ")
    if songs == 'q':
        break

    album = make_album(artist=artist, title=title, number_songs=songs)
    print()
    print(album)
