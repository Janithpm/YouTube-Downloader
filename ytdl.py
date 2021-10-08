
# This is a code for YouTube Video / Playlist Downloader
# This code belongs to Binary PlanetLk Youtube channel(https://www.youtube.com/channel/UClmzWslXQuL3zQsN7AHWb5Q/).
# Please protect the rights!
# Also please SUBSCRIBE and Support to channel.
# -----------------------------------------------------------------------------------------------------------------------------------
# This code block is only used for download and install the required python module if it isn't properly installed on your computer.
# Otherwise you can import module only using -> import youtube_dl
import os
import sys
try:
    import youtube_dl
except:
    print('Trying to download and install requred module : youtube_dl')
    os.system('python -m pip install youtube_dl')
    import youtube_dl
# -----------------------------------------------------------------------------------------------------------------------------------
args = sys.argv
argsLen = len(args[2:])
url = sys.argv[1]
defalut = sys.argv[2]


def getV_R():
    temp = '''
	Select Vido Quality : 
	1 - 720p
	2 - 360p
	3 - Audio only
	
	>>> '''
    return int(input(temp))


def getAuto_Sub():
    temp = input('Download Auto Generated Subtitle (Y / N) : ')
    if temp.lower() == 'yes' or temp.lower() == 'y':
        return 1
    elif temp.lower() == 'no' or temp.lower() == 'n':
        return 0
    else:
        return -1


# url = input('Enter the URL : ')
# add support for command line arguments
path = '%USERPROFILE%/Desktop/%(playlist_title)s/%(title)s.%(ext)s'
if defalut == 'd' or defalut == 'D':
    output = {'format': 'best', 'writeautomaticsub': False, 'outtmpl': path}
else:
    while True:
        vformat = getV_R()
        if vformat == 1:
            sub = getAuto_Sub()
            if sub == 1:
                output = {'format': 'best',
                          'writeautomaticsub': True, 'outtmpl': path}
                break
            elif sub == 0:
                output = {'format': 'best',
                          'writeautomaticsub': False, 'outtmpl': path}
                break
            else:
                print('Error : Invalied selection. Try again.')
                continue
        elif vformat == 2:
            sub = getAuto_Sub()
            if sub == 1:
                output = {'format': 'worst',
                          'writeautomaticsub': True, 'outtmpl': path}
                break
            elif sub == 0:
                output = {'format': 'worst',
                          'writeautomaticsub': False, 'outtmpl': path}
                break
            else:
                print('Error : Invalied selection. Try again.')
                continue
        elif vformat == 3:
            output = {'format': 'bestaudio/best', 'outtmpl': path}
            break
        else:
            print('Error : Invalied selection. Try again.')
            continue

if len(url) != 0:
    with youtube_dl.YoutubeDL(output) as y:
        y.download([url])

else:
    print('Invalied URL. Try again!')
