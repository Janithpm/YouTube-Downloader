import os
from argparse import ArgumentParser
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from rich.console import Console
from progress.spinner import MoonSpinner

parser = ArgumentParser()
parser.add_argument('-v', '--video', help="URL of YouTube Video")
parser.add_argument('-p', "--playlist", help="URL of YouTube Playlist")
parser.add_argument('-l', "--download-location", help="Download location")
parser.add_argument('-r', "--resolution",
                    help="Video Resolution", default=True)

args = parser.parse_args()
console = Console()

if args.video:
    V = YouTube(args.video, on_progress_callback=on_progress)
    VF = V.streams.filter(progressive=True)
    console.print(f"\n:Cinema: Title : {V.title}")
    Vstream = []
    for v in VF:
        # console.print(v)
        Vstream.append(
            {
                'itag': v.itag, 'resolution': v.resolution, 'v.mime_type': v.mime_type
            })

    console.print("\nSelect Video Resolution\n")
    for i, v in enumerate(Vstream):
        console.print(f"  :Cinema: [{i + 1}]\t- {v['resolution']}")

    tg = int(input("\n>>> "))
    stream = V.streams.get_by_itag(Vstream[tg - 1]['itag'])
    stream.download()

    # pprint(Vstream)

if args.playlist:
    p = Playlist(args.playlist)
    print(f'Downloading: {p.title},')
    temp = p.video_urls[0]
    V = YouTube(temp, on_progress_callback=on_progress)
    VF = V.streams.filter(progressive=True)

    Vstream = []
    for v in VF:
        # console.print(v)
        Vstream.append(
            {
                'itag': v.itag, 'resolution': v.resolution, 'v.mime_type': v.mime_type
            })

    console.print("\nSelect Video Resolution\n")
    for i, v in enumerate(Vstream):
        console.print(f"  :Cinema: [{i + 1}]\t- {v['resolution']}")

    tg = int(input("\n>>> "))
    print("")

    floderName = ""
    try:
        floderName = os.path.join(os.path.dirname(__file__), "Downloads")
    except:
        floderName = os.path.join(os.path.dirname(__file__), "Downloads")

    i = 1
    for url in p.video_urls:
        V = YouTube(url, on_progress_callback=on_progress)
        VF = V.streams.filter(progressive=True)
        console.print(f":Cinema: [{i}] Downloading ... : {V.title}\n")
        stream = V.streams.get_by_itag(Vstream[tg - 1]['itag'])
        stream.download(output_path=floderName, filename_prefix=f"{i} - ")
        i += 1
