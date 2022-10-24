from firstapp.settings.dev import SECRET_KEY
from .common import *
import os 

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []