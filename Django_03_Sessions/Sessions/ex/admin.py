from django.contrib import admin
from .models import CustomUser, Tip

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Tip)