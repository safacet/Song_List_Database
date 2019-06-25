from Classes import *
import time

song_list = Song_List()
print("""
************************************
Welcome to Song List

Selections:
1- Add Song
2- Delete Song
3- Sort All Songs
4- Search Songs
5- Total Length of Songs

Press q for quit...
************************************""")

while True:
    select = input("Your select:")
    if select == "q":
        print("Ending Program...")
        break
    elif select == "1":
        name = input("Name:")
        artist = input("Artist:")
        album = input("Album:")
        production = input("Production Company:")
        length = int(input("Length:"))
        new_song = Song(name, artist, album, production, length)
        song_list.add_song(new_song)
    elif select == "2":
        while True:
            name = input("Songs name that you want to delete:")
            song_list.search_song(name)
            inpt = input("Are you sure to delete this song? Y/N")
            if inpt == "N":
                print("Deleting Canceled!")
                break
            elif inpt == "Y":
                print("Song Deleting...")
                time.sleep(1)
                song_list.delete_song(name)
                print("Song has been deleted!")
                break
            else:
                print("Invalid Input!")

    elif select == "3":
        song_list.whole_list()
    elif select == "4":
        name = input("Songs name:")
        song_list.search_song(name)
    elif select == "5":
        song_list.total_length()
song_list.con.close()
