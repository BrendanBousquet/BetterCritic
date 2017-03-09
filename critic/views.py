from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from critic.models import Game

def index(request):
    games = Game.objects.all()
    context = RequestContext(request, {'list': games})
    template = loader.get_template('critic/test.html')
    return HttpResponse(template.render(context))

def test(request):
    template = loader.get_template('critic/test.html')
    return HttpResponse(template.render(request))