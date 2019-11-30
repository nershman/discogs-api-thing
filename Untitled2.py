import discogs_client
import random
import pafy
import vlc
import sys
if sys.platform == "darwin":
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets


    #vlc documentation... gotta guess and also use __dict__ to find what you need
    # https://www.videolan.org/developers/vlc/doc/doxygen/html/group__player.html#gga04208feb28bd3bcc1e2fc92e728b63e3a0143c79641bddc97f240e9b806ed44b2


#pafy.set_api_key()
#https://github.com/discogs/discogs_client
d = discogs_client.Client('DiscogsYoutubeShuffle/0.1', user_token=config.api_key)
#results = d.search('Stockholm By Night', type='release')

#get size of database things
#d.master()
#d.artist()


class getRandom:

            #figure out the range sizes
        artistSize=7050099
        releaseSize = 7050099

    def __init__(self):
        pass
    
    def artist(artistSize):
        while True:
            try:
                aID = random.randint(1,artistSize)
                artistName = d.artist(aID)
                print(artistName)
            except discogs_client.exceptions.HTTPError as err:
                if err.code == 404: #discogs_client.exceptions.HTTPError: 404: Artist not found.
                    continue
                else
                    raise
                    break
            break

    def release(releaseSize):
        while True:
            try:
                rID = random.randint(1,releaseSize)
                relName = d.release(rID)
                return relName 
            except discogs_client.exceptions.HTTPError as err:
                if err.code == 404:
                    continue
                else
                    raise
                    break
            break

    def video():

        while True: #loop retrieving random release until find one which contains videos
            a = randomRelease(releaseSize) #if this doesnt work look up how to refer to a clas va
            if len(a.videos) > 0
                break

        arrayLen = len(a.videos)
        vID = random.randint(0,arrayLen)
        URL = a.videos[vID].url
        return URL

    playVideo.p.play()
    print(vid)
    
    #use pafy library to stream youtube video to VLC
    #https://askubuntu.com/questions/518932/stream-audio-from-youtube
    

class Playlist:
    #this class intiilizaes an dynamic? array to keep track of what will be played next
     def __init__(self):
        n = 5
        self.arr = [0,0,0,0,0]


    def add(URL) #add a URL to bottom of stack, shift all others up.
        for i=1 in n:
            arr[i]=arr[i-1]
        arr[0] = URL

class Player:
    #this class intializes the VLC player, keeps track of what is playing, and opens the next song when a song ends.
    #when a song ends it just runs the Playlist.add(getRandom.video())
    def __init__:
        self.paused=False
        # https://www.codementor.io/princerapa/python-media-player-vlc-gtk-favehuy2b

            # on mac, a window needs to be manually opened
         #   if sys.platform == "darwin":
         #       vlcApp = QtWidgets.QApplication(sys.argv)
        #        vlcWidget = QtWidgets.QFrame()
        #        vlcWidget.resize(700,700)
        #        vlcWidget.show()
        #        p.set_nsobject(vlcWidget.winId())
    def playVideo(URL):
        vid = pafy.new(URL)#change to self.vid??
        vid = vid.getbestaudio().url

        self.p = vlc.MediaPlayer(vid)

    def continuousPlayback(playlist):

        arrlen = len(playlist.arr)

        #if length is 0 send an error.

        #if anything is playing, stop it


        #if the playback has ended.
        if self.p.get_state() == vlc.State.Ended
            #Playlist.advancePlaylist
            #play video in [0] position


    def skip():
        self.p.stop()

    def pause()
        self.p.pause()
        self.paused = True

    def togglePlayback()
        pass

def shuffleplay():
    playlist = Playist()
    playlist.add(getRandom.video())

    shufvlc = Player.continuousPlayback(playlist)



    # just a hwile script i guess
    URL = getRandomVideo()
    print("now playing:",URL)
    currentlyPlaying = playVideo(URL)
    #implement something which grabs the next URLS to play
    #add the next videos to VLC playlist maybe?, with a setting fo rhow many to keep
    #wait for input to terminate
    #use **args or something to add arguments later.
    while True

