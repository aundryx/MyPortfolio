from django.contrib import admin
from django.db.models import fields
from .models import Image, Link, Text

class imageAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'alt_text')
    fields = ('image', 'alt_text')

class linkAdmin(admin.ModelAdmin):
    list_display = ('id','links',)
    fields = ('links',)

class textAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'subtext', 'paragraph')
    fields = ('title', 'subtext', 'paragraph')

# Register your models here.

admin.site.register(Image, imageAdmin)
admin.site.register(Link, linkAdmin)
admin.site.register(Text, textAdmin)
