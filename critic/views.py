from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from critic.models import Game
import os.path

def index(request):
    games = Game.objects.all()
    context = RequestContext(request, {'list': games})
    template = loader.get_template('critic/index.html')
    return HttpResponse(template.render(context))

def game_detail(request, g):
    # g = request.GET.get('g')
    games = Game.objects.filter(game_name=g)
    context = RequestContext(request, {'list': games})
    template = loader.get_template('critic/game_detail.html')
    return HttpResponse(template.render(context))