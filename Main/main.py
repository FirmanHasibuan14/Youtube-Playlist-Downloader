from pytube import Playlist

def download_playlist(url):
    playlist_yt = Playlist(url)
    PLAYLIST = playlist_yt.video_urls
    length = len(PLAYLIST)
    for video in playlist_yt.videos:
        video1 = video.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        try:
            video1.download()
        except ValueError:
            print("there was an error downloading your youtube video")
        print(f"program will download {length} videos")
        for i,video1 in enumerate(PLAYLIST):
            print(i+1, f'{video1} is Downloaded......')
        for video in playlist_yt.videos:
            name_yt = video.title
            print(f"{name_yt} is Successfull Download")
        print("Finished")
url = input("Input your youtube playlist URL: \n")
download_playlist(url)
