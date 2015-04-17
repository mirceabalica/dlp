from django.contrib import admin
from .models import Screenshot, Domain


class ScreenshotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['domain']}),
        ('QA image', {'fields': ['qa_image']}),
        ('Production image', {'fields': ['production_image']}),
        ('Run id', {'fields': ['run_id']}),
        ('Date taken', {'fields': ['date_taken']})
    ]
    list_display = ('domain', 'qa_image', 'production_image', 'date_taken',
                    'run_id')
    list_filter = ['run_id', 'date_taken']

    def domain(self, obj):
        return obj.domain.url


class DomainAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Domain name', {'fields': ['url']}),
    ]
    list_display = ('url',)
    search_fields = ['url']


admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Domain, DomainAdmin)