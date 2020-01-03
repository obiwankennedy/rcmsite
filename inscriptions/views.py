from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Game, Event
from .modelform import GameForm

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the inscriptions index")


def showAllGame(request):
    allGames = Game.objects.order_by('-title').all()
    context = {
        'games': allGames,
    }
    return render(request, 'inscriptions/games.html',context)


def registrerForEvent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return HttpResponse("Bienvenue sur la fiche d'inscriptions pour %s:" % event_id)



def addGame(request):
    if request.method == 'POST':
        form = GameForm(resquest.POST)
        if form.is_valid():
            return HttpResponseRedirect('/addGame/')
    else:
        form = GameForm()
    return render(request, 'game.html', {'form': form})
#    model = Game
#    fields = ['title','description','punchline','type_text','imageUrl']
