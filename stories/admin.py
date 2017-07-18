from django.contrib import admin
from .models import Story
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'last_edited', 'featured', 'seen', 'votes')

admin.site.register(Story,StoryAdmin)
