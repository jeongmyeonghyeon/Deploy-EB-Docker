# debug.py
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 배포모드니까 DEBUG는 False
DEBUG = False
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

print('@@@@@@ DEBUG:', DEBUG)
print('@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
