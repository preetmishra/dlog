from django.contrib import admin
from django.db import models
from post import models as post_models
from martor.widgets import AdminMartorWidget

# Register your models here.

@admin.register(post_models.Entry)
class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ['title', 'date_created', 'publish']
    list_editable = ['publish']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(post_models.Tag)
