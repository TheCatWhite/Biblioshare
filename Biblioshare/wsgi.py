import os
import sys

# Chemin vers le dossier de ton projet sur PythonAnywhere
# Remplace "ton-username" par ton pseudo PythonAnywhere
project_home = '/home/theCatWhite/Biblioshare'

if project_home not in sys.path:
    sys.path.append(project_home)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Biblioshare.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
