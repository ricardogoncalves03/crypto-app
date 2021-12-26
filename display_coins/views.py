from django.views.generic import ListView
from display_coins.models import Coin

from .services import get_coins


class GetCoinsView(ListView):
    model = Coin
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'coins': get_coins(),
        }
        return context

class TestView(ListView):
    model = Coin
    template_name = "test_forms.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {
            'coins': get_coins(),
        }
        return context