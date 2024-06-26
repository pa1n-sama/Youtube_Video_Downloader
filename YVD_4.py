from pytube import YouTube
import yt_dlp

def download_video(url,output_path,format_):
    ydl_opts ={
        'format':'best',
        'outtmpl':output_path,
        'postprocessors':[{
            'key':'FFmpegVideoConvertor',
            'preferedformat':format_
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as YD:
        YD.download([url])

if __name__=='__main__':
    urls = input('Input the videos url: ').split(',')
    check = input('Video or Audio(V/A): ')
    for i in urls:
        if '&list' in i:
            playlist_check=input('This url is a playlist url, do you want to download the whole playlist(Y/N)?: ')
            if playlist_check.lower() in 'no':
                i = i.split('&')[0]
        file_name = YouTube(i).title.strip('/.(){}[]\\')
        if check.lower() in 'video':
            download_video(i,f'/home/pain/Downloads/Videos/{file_name}','mp4')
        elif check.lower() in 'audio':
            download_video(i,f'/home/pain/Downloads/Audios/{file_name}','mp3')
