from django.urls import path

from display_coins.views import GetCoinsView


urlpatterns = [
    path('', GetCoinsView.as_view(), name='coins view')
]
