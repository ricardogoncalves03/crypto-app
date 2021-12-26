# Django Admin
---

## Create a _superuser_

```bash
python manage.py createsuperuser
```

## Update admin.py file for the app to appear on the admin page

```python
# <app_name>/admin.py
from django.contrib import admin

from .models import <model_class>

admin.site.register(<model_class>)
```