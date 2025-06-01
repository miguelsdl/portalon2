from django.views.generic import ListView
from games.models.game import Game
from portalon import settings


class GameListView(ListView):
    model = Game
    template_name = 'games/index.html'
    paginate_by = settings.GAMES_PAGINATION

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['page_obj']  # Ensures compatibility with your template
        return context