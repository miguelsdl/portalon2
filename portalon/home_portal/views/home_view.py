from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        context = {
            'year': 2025,
            'title': 'Inicio',
            'description': 'Portal de noticias y contenido',
        }
        return render(request, 'home_portal/index.html', context)
