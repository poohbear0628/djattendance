from django.contrib import admin
from .models import Class

class ClassAdmin(admin.ModelAdmin):
    exclude = ['type']

    # Automatically type class event objects saved.
    def save_model(self, request, obj, form, change):
        obj.type = 'C'
        obj.save()

#admin.site.register(Class)
admin.site.register(Class, ClassAdmin)