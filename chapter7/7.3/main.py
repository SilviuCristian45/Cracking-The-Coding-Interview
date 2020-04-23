#Design a musical juke box using object oriented principles
class MusicalJukeBox():
    music_track = []
    current_music = 0
    volume = 50

    def Play(self):
        print(str(self.music_track[self.current_music]))

    def Next(self):
        self.current_music += 1

    def Previous(self):
        self.current_music -= 1
    
    def AdjustVolume(self , new_volume):
        self.volume = new_volume
    #add in song
    def AddSong(self,song):
        self.music_track.append(song)
    #what song to delete
    def DeleteSong(self,song):
        if self.music_track.index(song):
            self.music_track.remove(song)
        else :
            print("This song is not in the playlist .")