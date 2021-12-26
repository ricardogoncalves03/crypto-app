# Migrations
---

## Activating models
### 1. Create migrations file**
```bash
python manage.py makemigrations <app_name>
```

### 2. Build the actual database 
```bash
python manage.py migrate
```

<br></br>
**Note that you don’t have to include a name after `makemigrations`. If you simply run `python
manage.py makemigrations`, a migrations file will be created for all available changes throughout
the Django project. That is fine in a small project such as ours with only a single app, but most
Django projects have more than one app! Therefore ,if you made model changes in multiple apps
the resulting migrations file would include all those changes! This is not ideal. Migrations file
should be as small and concise as possible as this makes it easier to debug in the future or even
roll back changes as needed. Therefore, as a best practice, adopt the habit of always including
the name of an app when executing the makemigrations command!