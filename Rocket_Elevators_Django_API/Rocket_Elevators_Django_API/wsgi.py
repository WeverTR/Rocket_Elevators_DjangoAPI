"""
WSGI config for Rocket_Elevators_Django_API project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rocket_Elevators_Django_API.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
