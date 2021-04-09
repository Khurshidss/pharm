from django.urls import path

from .views import DistrictListView

app_name = "regions"

urlpatterns = [
    path("district/", DistrictListView.as_view(), name="list"),

]
