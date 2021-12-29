from django.urls import path

from accounts.views import SignUpCreateView


urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup')
]
