from django.urls import path

from display_coins.views import DisplayCoinsView, DisplayCoinsCreateView


urlpatterns = [
    path('', DisplayCoinsView.as_view(), name='home'),
    path('new/', DisplayCoinsCreateView.as_view(), name='coin_new')
]
