import sqlite3


class Song():
    def __init__(self, name, artist, album, production, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.production = production
        self.length = length
    def __str__(self):
        minute  = self.length // 60
        second = self.length % 60
        return """Song Infos:
        Song Name: {}
        Artist: {}
        Album: {}
        Production Company: {}
        Length: {} . {}""".format(self.name, self.artist, self.album, self.production, minute, second)

class Song_List():
    def __init__(self):
        self.connect()
    def connect(self):
        self.con = sqlite3.connect("Song_List.db")
        self.cursor = self.con.cursor()
        query = "create table if not exists songs(Name TEXT, Artist TEXT, Album TEXT, Production TEXT, Length INT)"
        self.cursor.execute(query)
        self.con.commit()
    def add_song(self, song):
        query = "Insert into songs values(?, ?, ?, ?, ?)"
        self.cursor.execute(query, (song.name, song.artist, song.album, song.production, song.length))
        self.con.commit()
    def delete_song(self, name):
        query = "delete from songs where Name = ?"
        self.cursor.execute(query,(name,))
        self.con.commit()
    def whole_list(self):
        query = "select * from songs"
        self.cursor.execute(query)
        song_list = self.cursor.fetchall()
        if len(song_list) == 0:
            print("There are no songs on the list.")
        else:
            for i in song_list:
                minute = i[4] // 60
                second = i[4] % 60
                print("{} - {} - {} - {} - {}:{} ".format(i[0], i[1], i[2], i[3], minute, second))
    def search_song(self, name):
        query = "select * from songs where Name = ?"
        self.cursor.execute(query, (name,))
        song_list = self.cursor.fetchall()
        song = Song(song_list[0][0], song_list[0][1], song_list[0][2], song_list[0][3], song_list[0][4])
        print(song)
    def total_length(self):
        query = "Select * from songs"
        self.cursor.execute(query)
        song_list = self.cursor.fetchall()
        total_length = 0
        for i in song_list:
            total_length += i[4]
        minute = total_length // 60
        second = total_length % 60
        print("Total length of the songs: {} Minutes {} Seconds".format(minute, second))

