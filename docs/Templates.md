# Create single project-level templates directory
---

## Create directory and html file

```bash
(django-skeleton) $ mkdir templates
```
```bash
(django-skeleton) $ touch templates/base.html
```

## Tell Django the new location of our new templates directory

```python
# config/settings.py
TEMPLATES = [
{
...
'DIRS': [str(BASE_DIR.joinpath('templates'))], # new
...
},
]
```