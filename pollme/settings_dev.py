from .settings import *

# Set debug to True for development
DEBUG = True

# Add development-specific applications
INSTALLED_APPS += ['debug_toolbar',]

# Add development-specific middleware
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
