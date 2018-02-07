'''
Heavy Meta main views module
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from hm_web.models import Song

# Create your views here.
def index(request):
    '''
    Index view
    '''
    if request.user.is_authenticated:
        return redirect('/songs')

    return render(request, 'hm_web/index.html', {})


class SongList(LoginRequiredMixin, ListView):
    '''
    View a list of songs
    '''
    model = Song


@login_required
def song(request, pk):
    '''
    View for a single song
    '''
    try:
        the_song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        raise Http404("Song does not exist")

    return render(request, 'hm_web/song.html', {'song': the_song})
