=====
clickanalysis
=====


Quick start
-----------

1. Add "clickanalysis" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'clickanalysis'
  }

2. Add `clickanalysis.middleware.ClickAnalysisMiddleware` to the MIDDLEWARE_CLASSES tuple in your settings file.

3. Run `python manage.py syncdb` to create myblog's models.