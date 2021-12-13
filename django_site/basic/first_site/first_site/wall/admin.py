from django.contrib import admin

from .models import Wall
from .models import Rubric


class WallAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(Wall, WallAdmin)
admin.site.register(Rubric)
