from django.contrib import admin
from learn import models
# Register your models here.


class PublishAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ['city']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['city']}),
    ]


admin.site.register(models.Publish, PublishAdmin)
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Question)
admin.site.register(models.Choice)

