from django.http import HttpResponse
from . models import Album

def index(request): # always pass this parameter
    all_album= Album.objects.all()
    html=''
    for album in all_album: # display all the albums in the database
        url='/music/'+ str(album.id)+ '/'
        html+='<a href={}>{}</a><br>'.format(url,album.album_title)

    return HttpResponse(html)

def detail(request , album_id):
    return HttpResponse("<h1>details for album id: "+ str(album_id)+"</h1>")