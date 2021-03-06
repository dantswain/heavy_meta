'''
Routing configuration
'''

# pylint: disable=invalid-name

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',
         auth_views.LoginView.as_view(template_name='hm_web/login.html'),
         name='login'),
    path('logout',
         auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),
    path('songs', views.SongList.as_view(), name='songs'),
    path('songs/<int:pk>', views.song, name='song'),
]
