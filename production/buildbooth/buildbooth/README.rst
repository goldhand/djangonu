buildbooth
==============================

essaytool


LICENSE: BSD

Deployment
------------

* heroku create
* heroku addons:add heroku-postgresql:dev
* heroku addons:add pgbackups
* heroku addons:add sendgrid:starter
* heroku pg:promote HEROKU_POSTGRESQL_COLOR
* heroku config:add DJANGO_CONFIGURATION=Production
* heroku config:add DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
* heroku config:add DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
* heroku config:add DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
* heroku config:add DJANGO_AWS_STORAGE_BUCKET_NAME=BUCKET
* git push heroku master
* heroku run python buildbooth/manage.py syncdb --noinput --settings=config.settings
* heroku run python buildbooth/manage.py migrate --settings=config.settings
* heroku run python buildbooth/manage.py collectstatic --settings=config.settings

Run this script: (TODO - automate this)

.. code-block:: python

    from django.contrib.sites.models import Site
    site = Site.objects.get()
    site.domain = "django.nu/buildbooth"
    site.name = "buildbooth"
    site.save()