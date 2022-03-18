from django.contrib import admin
from .models import Profile, Resident
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Profile)
admin.site.register(Resident)
