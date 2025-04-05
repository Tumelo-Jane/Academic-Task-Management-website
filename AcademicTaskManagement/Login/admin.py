from django.contrib import admin
from .models import signup_details
from .models import login_details

# Register your models here.
admin.site.register(signup_details)
admin.site.register(login_details)
