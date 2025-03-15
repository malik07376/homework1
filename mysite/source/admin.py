from django.contrib import admin
from .models import Director,Actor

class IsActiveFilter(admin.SimpleListFilter):
    title = 'Active Status'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return (
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.filter(is_active=True)
        if self.value() == 'inactive':
            return queryset.filter(is_active=False)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('director_name', 'is_active')
    list_filter = ('is_active', IsActiveFilter)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor_name', 'is_active')
    list_filter = ('is_active', IsActiveFilter)

admin.site.register(Director,DirectorAdmin)
admin.site.register(Actor,ActorAdmin)
# Register your models here.
