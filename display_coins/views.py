from django.shortcuts import render
from django.views.generic import TemplateView

from display_coins.services import get_coins


class GetCoinsView(TemplateView):
    template_name = "coins.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'coins': get_coins(),
        }
        return context
