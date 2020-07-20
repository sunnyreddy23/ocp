from django.contrib import admin
from .models import Topic, Preference, Medium
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    pass 

class PreferenceAdmin(admin.ModelAdmin):
    pass

class MediumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)
admin.site.register(Preference, PreferenceAdmin)
admin.site.register(Medium, MediumAdmin)