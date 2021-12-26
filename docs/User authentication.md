# Built-in user authentication system
---

Django provides us with a default view for a log in page via `LoginView`. All we need to add are a URLpattern for the auth system, a log in template, and a small update to our _config/settings.py_ file.

## Update config/urls.py file

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')) # new  
]
```

## Create registration directory for _login.html_

```bash
(django-skeleton) $ mkdir templates/registration
```

```bash
(django-skeleton) $ touch templates/registration/login.html
```

## Redirect the user upon successful log in and log out

```python
# config/settings.py
LOGIN_REDIRECT_URL = '<url_name>' # e.g. 'home'
```

```python
# config/settings.py
LOGOUT_REDIRECT_URL = '<url_name>' # e.g. 'home'
``` 