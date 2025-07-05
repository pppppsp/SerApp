from django.contrib import admin
from user.models import *


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fields=['last_name']


# Register your models here.
