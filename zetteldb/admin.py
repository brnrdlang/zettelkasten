from django.contrib import admin

from .models import ZettelThread, Zettel
# Register your models here.

admin.site.register(ZettelThread)
admin.site.register(Zettel)
