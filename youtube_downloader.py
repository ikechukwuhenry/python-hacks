import yt_dlp

# Enter the url for download
url = input("Enter video url: ")

download_directory = "/Users/mac/Download"
ydl_opts = {
    'outtmpl':f'{download_directory}/%(title)s.%(ext)s',
    'format':'mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully")