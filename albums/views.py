from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm


def album_list(request):
    # In the line below we could have filtered which albums to get, but we got all of them
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {"album": album})


# Finish
def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.artist = request.user
            album.release_date = request.user
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {'form': form})
