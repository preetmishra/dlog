from django.contrib import admin
from post import models as post_models
# Register your models here.

@admin.register(post_models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'publish']
    list_editable = ['publish']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(post_models.Tag)
