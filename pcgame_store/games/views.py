from django.forms.models import model_to_dict
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Game


def index(request):
    return HttpResponse("Hello, world. You're at the cew index.")


def detail(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        game = model_to_dict(game)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    return JsonResponse(game, safe=False)


# def index_by_user(request):
