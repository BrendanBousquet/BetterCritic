from django.conf.urls import url

from critic import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.game_detail, name='game_detail'),
]