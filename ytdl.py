
# This is a code for YouTube Video / Playlist Downloader
# This code belongs to Binary PlanetLk Youtube channel(https://www.youtube.com/channel/UClmzWslXQuL3zQsN7AHWb5Q/).
# Please protect the rights!
# Also please SUBSCRIBE and Support to channel.
#-----------------------------------------------------------------------------------------------------------------------------------
# This code block is only used for download and install the required python module if it isn't properly installed on your computer.
# Otherwise you can import module only using -> import youtube_dl  
import os
try:
        import youtube_dl
except:
        print('Trying to download and install requred module : youtube_dl')
        os.system('python -m pip install youtube_dl')
        import youtube_dl
#-----------------------------------------------------------------------------------------------------------------------------------

#geting url
url = input('Enter the URL : ')

#getiing other infomations
while True:
	vformat = input('Select video quality (720p/360p) : ')
	sub = input('Download auto genarated subtitle (y/n) : ')

	if vformat == '720p':
		if sub == 'y':
			output = {'format':'best', 'writeautomaticsub':True, 'outtmpl':'./%(playlist_title)s/%(title)s.%(ext)s'}
			break
		elif sub == 'n':
			output = {'format':'best', 'writeautomaticsub':False, 'outtmpl':'./%(playlist_title)s/%(title)s.%(ext)s'}
			break
		else:
			print('Error : Invalied selection. Try again.')
			continue
	elif vformat == '360p':
		if sub == 'y':
			output = {'format':'worst', 'writeautomaticsub':True, 'outtmpl':'./%(playlist_title)s/%(title)s.%(ext)s'}
			break
		elif sub == 'n':
			output = {'format':'worst', 'writeautomaticsub':False, 'outtmpl':'./%(playlist_title)s/%(title)s.%(ext)s'}
			break
		else:
			print('Error : Invalied selection. Try again.')
			continue
	else:
		print('Error : Invalied selection. Try again.')
		continue

#downloading the video / playlist
if len(url) != 0:
	with youtube_dl.YoutubeDL(output) as y:
		y.download([url])

else:
	print('Invalied URL.')
