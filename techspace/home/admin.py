from django.contrib import admin

from home.models import Contact
from home.models import Phone
# Register your models here.

admin.site.register(Contact)
admin.site.register(Phone)