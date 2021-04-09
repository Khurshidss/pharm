from django.contrib import admin

from .models import Region, District


class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_region")
    list_filter = ("region",)
    search_fields = ("name",)

    def get_region(self, obj):
        return obj.region.name


admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
