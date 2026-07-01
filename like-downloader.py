import yt_dlp

def download_likes(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'outtmpl': '%(title)s.%(ext)s',
        'cookiesfrombrowser': ('firefox',),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"{url.rstrip('/')}/likes"])

if __name__ == "__main__":
    download_likes("https://soundcloud.com/newdakha") # edit your name
