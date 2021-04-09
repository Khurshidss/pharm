from django.views.generic import ListView

from regions.models import District


class DistrictListView(ListView):
    template_name = "district_list.html"

    def get_queryset(self):
        region_id = self.request.GET.get("region")
        return District.objects.filter_by_region(region_id)
