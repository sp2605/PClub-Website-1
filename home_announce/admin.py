from django.contrib import admin
from .models import Announcement,Daily
# Register your models here.
admin.site.register(Announcement)
admin.site.register(Daily)
admin.site.site_header='Programming Club Website'