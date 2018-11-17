from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(DinderGroup)
admin.site.register(DinderEvent)
admin.site.register(DinderProfile)