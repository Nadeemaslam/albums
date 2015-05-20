import os
import sys
import site
import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'albums.settings'
site.addsitedir('/srv/www/gallery/lib/python2.7/site-packages')
sys.path.append('/srv/www/albums')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

