=====
clickanalysis
=====

This package provides an easy way to track all the link clicks you want to track whether they exists in site or in your email campaigns

Quick start
-----------

1. Add "clickanalysis" to INSTALLED_APPS:
  INSTALLED_APPS = {
    ...
    'clickanalysis',
    ...
  }

2. Add `clickanalysis.middleware.ClickAnalysisMiddleware` to the MIDDLEWARE_CLASSES tuple in your settings file.

3. Run `python manage.py syncdb` to create required tables.

4. After all this you are set to track all the clicks. You may be seeing two tables created in admin site "Campaign" and "ClickTracking".

5.
