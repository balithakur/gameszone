from myfirstproject.settings import *

from decouple import config

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = ["gamerszone.up.railway.app"]


