from django.urls import path
from games.views.game_list_view import GameListView

urlpatterns = [
    path('', GameListView.as_view(), name='games_index'),
]
