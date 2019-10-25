from django.contrib import admin
from .models import Profile
# Registras los modelos aquí para que puedan visualizarce dentro del admin
admin.site.register(Profile)