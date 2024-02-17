from django.shortcuts import render
from pytube import YouTube
from datetime import timedelta


def homepage(request):
    return render(request, 'index.html', {'video_data': {}})


def video(request):

    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        # vquaity = request.POST.get('vqlty')

        try:
            youtube = YouTube(video_url)
            # video_streams = youtube.streams.filter(
            #     file_extension="mp4", progressive=True)
            highresvid = youtube.streams.get_highest_resolution()
            title = youtube.title
            duration = youtube.length
            size = highresvid
            thumb_nail = youtube.thumbnail_url
            duration = timedelta(seconds=duration)
            # highresvid.download('~download')
            video_data = {'title': title,
                          'thumb_nail': thumb_nail, 'duration': duration, 'resolution': highresvid.resolution, 'filetype': highresvid.mime_type, 'url': highresvid.url}
            # print(video_streams.url)
        except Exception as e:
            print('Exception found', e)
    return render(request, 'video_detail.html', {'video_data': video_data})
