'''
Heavy Meta main views module
'''

from django.views.generic import ListView
from django.shortcuts import render

from hm_web.models import Song

# Create your views here.
def index(request):
    '''
    Index view
    '''
    return render(request, 'hm_web/index.html', {})


class SongList(ListView):
    '''
    View a list of songs
    '''
    model = Song
