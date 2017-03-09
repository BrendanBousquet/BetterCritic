from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from critic.models import Game

def index(request):
    games = Game.objects.all()
    context = RequestContext(request, {'list': games})
    template = loader.get_template('critic/index.html')
    return HttpResponse(template.render(context))

def game_detail(request):
    template = loader.get_template('critic/game_detail.html')
    return HttpResponse(template.render(request))