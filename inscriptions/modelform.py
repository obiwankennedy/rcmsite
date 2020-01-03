from django.forms import ModelForm
from .models import Game
from .models import Event


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title','description','punchline','type_text','imageUrl']



class EventFrom(ModelForm):
    class Meta:
        model = Event
        fields = ['name','date_start','date_end']
