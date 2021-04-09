from django.urls import path

from .views import MedicineList, PharmacyMedicineDetail

app_name = "medicines"

urlpatterns = [
    path("", MedicineList.as_view(), name="list"),
    path("<int:pk>/", PharmacyMedicineDetail.as_view(), name="detail"),

]
