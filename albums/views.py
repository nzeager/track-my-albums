from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
from django.db.models.functions import Lower


def album_list(request):
    # In the line below we could have filtered which albums to get, but we got all of them
    albums = Album.objects.all().order_by(Lower('title'))
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {"album": album})


def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {'form': form})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/create_album.html', {'form': form})


def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')
