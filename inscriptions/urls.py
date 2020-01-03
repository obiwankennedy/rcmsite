from django.urls import path

from . import views
from . import modelform

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:event_id>/inscriptions/', views.registrerForEvent, name='inscriptions'),
        path('jeux', views.showAllGame, name='Tous les jeux'),
        path('addGame', views.addGame, name='Ajouter un jeu')
        ]
