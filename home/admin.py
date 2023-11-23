from django.contrib import admin

from .models import City, Image, Real_estate, Time, Visit, Visualization


@admin.register(Real_estate)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('street', 'price', 'room', 'dimension', 'city', 'location',)
    list_editable = ('price', 'location',)
    list_filter = ('city', 'location',)


admin.site.register(Visualization)
admin.site.register(City)
admin.site.register(Image)
admin.site.register(Time)
admin.site.register(Visit)
