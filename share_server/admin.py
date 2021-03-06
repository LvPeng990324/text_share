from django.contrib import admin
from .models import Text


@admin.register(Text)
class TextInformation(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'create_time', 'to_top', 'is_deleted',)
