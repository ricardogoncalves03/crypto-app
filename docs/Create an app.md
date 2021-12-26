# Create a New App
---

## Command line

```bash
python manage.py startapp <app_name>
```

## Explicitly add it to the project 

```python
# config/settings.py
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'<app_name>', # new
]
```

## Create additional files

Usually _urls.py_ for each app