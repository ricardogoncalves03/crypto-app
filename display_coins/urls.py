from django.urls import path

from display_coins.views import (DisplayCoinsDetailView,
                                 DisplayCoinsUserListView,
                                 DisplayCoinsView, DisplayCoinsCreateView)


urlpatterns = [
    path('coin/<int:pk>', DisplayCoinsDetailView.as_view(), name='coin_detail'),
    path('new/', DisplayCoinsCreateView.as_view(), name='coin_new'),
    path('', DisplayCoinsView.as_view(), name='home'),
    path('coins', DisplayCoinsUserListView.as_view(), name='coin_user_list')
]
