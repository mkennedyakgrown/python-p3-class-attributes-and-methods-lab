class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(Song)
        Song.add_to_genres(Song, genre)
        Song.add_to_artists(Song, artist)

    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            Song.add_to_genre_count(Song, genre)

    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1
        else:
            Song.add_to_artist_count(Song, artist)

    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] += 1

    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] += 1

    def genre_count(cls):
        pass

    def artist_count(cls):
        pass
