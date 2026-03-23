from django.contrib import admin
from .models import Application, Notification, Registration, Session, User
# Register your models here.
admin.site.register(Application)
admin.site.register(Notification)
admin.site.register(Registration)
admin.site.register(Session)
admin.site.register(User)