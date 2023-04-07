from django.contrib import admin
from .models import Profile, feedback

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone')
admin.site.register(Profile, ProfileAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'timestamp')

admin.site.register(feedback, FeedbackAdmin)
