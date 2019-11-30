import discogs_client
import random
import pafy
import vlc
import sys
if sys.platform == "darwin":
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets

#pafy.set_api_key()
#https://github.com/discogs/discogs_client
d = discogs_client.Client('DiscogsYoutubeShuffle/0.1', user_token="PLACEHOLDER")
results = d.search('Stockholm By Night', type='release')

#get size of database things
#d.master()
#d.artist()

artistSize=7050099
releaseSize = 7050099

def randomArtist(artistSize):
#trycatch artistnotfound 404
    aID = random.randint(1,artistSize)
    artistName = d.artist(aID)
    print(artistName)
#it seems some artist ID numbers dont exist such as 194325. just catch this error and try again.

def randomRelease(releaseSize):
    rID = random.randint(1,releaseSize)
    relName = d.release(rID)
    return relName 
    
def getRandomVideo():
    releaseSize=7050099
    a = randomRelease(releaseSize) #how to amke this a global variable? like in java lol.
    arrayLen = len(a.videos) #starts at 0
   # if arrayLen NOT NULL (?)
    vID = random.randint(0,arrayLen)
    URL = a.videos[vID].url
    return URL

def playVideo(URL):
    vid = pafy.new(URL)
    vid = vid.getbestaudio().url

    playVideo.p = vlc.MediaPlayer(vid)



# on mac, a window needs to be manually opened
 #   if sys.platform == "darwin":
 #       vlcApp = QtWidgets.QApplication(sys.argv)
#        vlcWidget = QtWidgets.QFrame()
#        vlcWidget.resize(700,700)
#        vlcWidget.show()
#        p.set_nsobject(vlcWidget.winId())
    playVideo.p.play()
    print(vid)
    
    #use pafy library to stream youtube video to VLC
    #https://askubuntu.com/questions/518932/stream-audio-from-youtube
    
def shuffle():
    # just a hwile script i guess
    URL = getRandomVideo()
    print("now playing:",URL)
    currentlyPlaying = playVideo(URL)
    #implement something which grabs the next URLS to play
    #add the next videos to VLC playlist maybe?, with a setting fo rhow many to keep
    #wait for input to terminate
    #use **args or something to add arguments later.




