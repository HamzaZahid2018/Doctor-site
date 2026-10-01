from django.contrib import admin
from .models import Service, Qualification, ClinicInfo

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', 'title')

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('degree_title', 'institution', 'country', 'order')
    ordering = ('order', 'degree_title')

@admin.register(ClinicInfo)
class ClinicInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone_number', 'city')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
