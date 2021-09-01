from django.contrib import admin

from .models import Player, NameStatic


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'nick', 'proffesion', 'static_id')
    list_display_links = ('name', 'nick')
    search_fields = ('name', 'nick',)


admin.site.register(Player, PlayerAdmin)
admin.site.register(NameStatic)
