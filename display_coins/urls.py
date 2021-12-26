from django.urls import path

from display_coins.views import GetCoinsView, TestView


urlpatterns = [
    path('', GetCoinsView.as_view(), name='coins view'),
    path('test/', TestView.as_view(), name='test_forms')
]
