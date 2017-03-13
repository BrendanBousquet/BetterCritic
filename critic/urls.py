from django.conf.urls import url

from critic import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^game_detail(?:/(?P<g>[a-zA-Z]+)/)?', views.game_detail, name='game_detail'),
    url(r'^game_detail/(?P<g>.+)/$', views.game_detail, name='game_detail'),

]