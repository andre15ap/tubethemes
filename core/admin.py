from django.contrib import admin

# Register your models here.
from .models import Tube, Theme

admin.site.register(Tube)
admin.site.register(Theme)