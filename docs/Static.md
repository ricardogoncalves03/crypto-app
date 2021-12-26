# Static Files
---

## Create a static directory

```bash
mkdir static
```

## Tell Django to look for this new folder we just created

```python
# config/settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))] # new
```