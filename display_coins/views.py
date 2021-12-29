from django import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from display_coins.models import Coin
from django.shortcuts import get_object_or_404, redirect

from .services import get_coins


class DisplayCoinsView(ListView):
    model = Coin
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'coins': get_coins(),
        }
        return context


class DisplayCoinsCreateView(CreateView):
    model = Coin
    template_name = "coin_new.html"
    fields = ['name']

    def post(self, request):
        form_input_name = request.POST['name'].lower()
        for coin in get_coins():
            if form_input_name == coin['name'].lower():
                Coin.objects.get_or_create(
                    rank=coin['market_cap_rank'],
                    logo=coin['image'],
                    name=form_input_name,
                    price=coin['current_price'],
                    market_cap=coin['market_cap']
                )
                return redirect('home')
