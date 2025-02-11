from django.contrib import admin
from .models import UserProfile,Education,Experience

# Register your models here.
admin.site.register([UserProfile,Education,Experience])