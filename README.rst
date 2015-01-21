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


5. You can start by creating a campaign in Campaign table which will generate a unique ID for you, just copy that and keep it in clipboard to paste in the links.


6. Now whatever links you want to track just append this param to those links /link/?cid=campaign_unique_id


You will start getting tracking data soon when users start clicking through the links!!!
