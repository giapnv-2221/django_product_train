from django.contrib import admin, sites
from . import models

admin.site.register(models.Products)
admin.site.register(models.Categories)
