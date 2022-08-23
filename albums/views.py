from django.shortcuts import render


def album_list(request):
    return render(request, 'albums/album_list.html', {})
