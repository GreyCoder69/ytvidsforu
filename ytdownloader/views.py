from django.shortcuts import render
from pytube import YouTube
from pathlib import Path
import asyncio
import math
import glob
import os
from django.conf import settings
from django.http import FileResponse,HttpResponse
from django.utils.encoding import smart_str

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    Media = os.path.join(settings.MEDIA_ROOT)
    if request.method == 'POST':
        try:
            lid = os.listdir(Media)
            for item in lid:
                if item.endswith(".mp4"):
                    os.remove(f'{Media}/{item}')
        except:
            pass            

        if 'video_url_d' in request.POST:
            video_url = request.POST['video_url_d']
        else:    
            video_url = request.POST['video_url']
        try:            
            yt = YouTube(video_url)
            thumbnail_url = yt.thumbnail_url
            title = yt.title
            dd = str(yt.streams.all)
            p144 = '144p'
            p240 = '240p'
            p360 = '360p'
            p480 = '480p'
            p720 = '720p'
            p1080 = '1080p'
            if p144 in dd:
                res144 = True
                s144 = yt.streams.filter(res="144p").first()
                size1 = math.trunc(s144.filesize / 1048000)          
            else:
                size1 = None
                res144 = False    
            if p240 in dd:
                res240 = True
                s240 = yt.streams.filter(res="240p").first()
                size2 = math.trunc(s240.filesize / 1048000) 
            else:
                size2 = None
                res240 = False    
            if p360 in dd:
                s360 = yt.streams.filter(res="360p").first()
                size3 = math.trunc(s360.filesize / 1048000)
                res360 = True
            else:
                size3 = None
                res360 = False    
            if p480 in dd:
                s480 = yt.streams.filter(res="480p").first()
                size4 = math.trunc(s480.filesize / 1048000)
                res480 = True
            else:
                size4 = None
                res480 = False    
            if p720 in dd:
                s720 = yt.streams.filter(res="720p").first()
                size5 = math.trunc(s720.filesize / 1048000)
                res720 = True
            else:
                size5 = None
                res720 = False    
            if p1080 in dd:
                s1080 = yt.streams.filter(res="1080p").first()
                size6 = math.trunc(s1080.filesize / 1048000)
                res1080 = True
            else:
                size6 = None
                res1080 = False
            if 'audio' in dd:
                aud = yt.streams.get_audio_only()
                sizea = math.trunc(aud.filesize / 1048000)                             
            if 'formatradio' in request.POST:
                fr = request.POST['formatradio']
                if fr == 'audio':
                    ysss = yt.streams.get_audio_only()
                    ysss.download(Media)
                    if os.path.exists(f'{Media}/{title}.mp4'):
                        response = FileResponse(open(f'{Media}/{title}.mp4','rb'),as_attachment=True)
                        return response
                elif fr == 'video':
                    q = request.POST['qualityRadio']
                    yss = yt.streams.filter(res=q).first()
                    yss.download(Media)
                    if os.path.exists(f'{Media}/{title}.mp4'):
                        response = FileResponse(open(f'{Media}/{title}.mp4','rb'),as_attachment=True)
                        return response                    
                else:
                    pass    
                    
            else:
                return render(request,'home.html',{'title':title,'thumbnail_url':thumbnail_url,'video_url':video_url,'p144':res144,'p240':res240,'p360':res360,'p480':res480,'p720':res720,'p1080':res1080,'size1':size1,'size2':size2,'size3':size3,'size4':size4,'size5':size5,'size6':size6,'sizea':sizea})
        
        except:
            failed = True
            return render(request,'home.html',{'failed':failed})


    else:
        failed = False     
        return render(request,'home.html',{'failed':failed})
    
