from django.conf.urls import url

from critic import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]