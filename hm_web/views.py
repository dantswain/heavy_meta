'''
Heavy Meta main views module
'''

from django.contrib.auth.mixins import LoginRequiredMixin
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
