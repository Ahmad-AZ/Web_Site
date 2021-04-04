from django.contrib import admin

from .models import  Album,Song

admin.site.register(Album) # register the Album in the admin site to make appear in the admin site
admin.site.register(Song)