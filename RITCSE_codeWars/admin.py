from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from RITCSE_codeWars.models import Contest, Question

admin.site.register(Contest)
admin.site.register(Question)
