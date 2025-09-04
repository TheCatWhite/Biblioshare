from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Ressource)
admin.site.register(Telechargement)
admin.site.register(Favori)