from django.shortcuts import render
from .models import Album


def album_list(request):
    # In the line below we could have filtered which albums to get, but we got all of them
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})
