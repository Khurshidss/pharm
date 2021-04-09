from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django_filters.views import FilterView
from .filters import MedicineFilter
from .models import PharmacyMedicine


class MedicineList(FilterView):
    paginate_by = 15
    template_name = "index.html"
    filterset_class = MedicineFilter
   # price = price.objects.order_by()
    
    def get_queryset(self):
        return PharmacyMedicine.objects.get_pharmacy_and_medicine()


class PharmacyMedicineDetail(DetailView):
    template_name = "detail.html"

    def get_object(self, queryset=None):
        print(self.kwargs.get("pk"))
        return PharmacyMedicine.objects.filter(pk=self.kwargs.get("pk")).select_related("pharmacy", "medicine").first()
