import django_filters
from django.forms import TextInput, Select
from django_filters import FilterSet

from medicines.models import PharmacyMedicine, Medicine
from regions.models import Region, District


class MedicineFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',
                                      field_name="pharmacy_medicine",
                                      widget=TextInput(attrs={
                                          "class": "form-control mx-0 search-input",
                                          "placeholder": "Enter medicine name"
                                      }))

    regions = django_filters.ModelChoiceFilter(queryset=Region.objects.all(),
                                               widget=Select(attrs={
                                                   "class": "form-control",
                                                   "id": "region"
                                               }), method="filter_by_region")

    districts = django_filters.ModelChoiceFilter(
        queryset=District.objects.none(),
        widget=Select(attrs={
            "class": "form-control",
            "id": "district"
        }), method="filter_by_district")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        region_id = self.request.GET.get("regions")
        if region_id:
            self.filters['districts'].queryset = District.objects.filter(
                region_id=region_id)
        else:
            self.filters['districts'].queryset = District.objects.all()
    class Meta:
        model = PharmacyMedicine
        fields = ["title", "regions", "districts", ]

    def filter_by_region(self, queryset, name, value):
        base_query = queryset
        if value:
            base_query = queryset.filter(pharmacy__district__region_id=value)
        return base_query

    def filter_by_district(self, queryset, name, value):
        base_query = queryset
        if value:
            base_query = queryset.filter(pharmacy__district_id=value)
        return base_query
