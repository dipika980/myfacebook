from django.contrib import admin
from social.models import Userpost, userprofile
# Register your models here.
admin.site.register(userprofile)
admin.site.register(Userpost)

