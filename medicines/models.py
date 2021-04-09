from django.db import models


class Medicine(models.Model):
    class MedicineType(models.TextChoices):
        Tablet = "Tablet"
        Syrup = "Syrup"
        Capsule = "Capsule"
        Other = "Other"

    medicine_type = models.CharField(choices=MedicineType.choices,
                                     max_length=15,
                                     default=MedicineType.Other)
    barcode = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}"


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    district = models.ForeignKey("regions.District",
                                 on_delete=models.CASCADE,
                                 related_name="pharmacies")
    address = models.CharField(max_length=255)
    works_from = models.TimeField(blank=True, null=True)
    works_to = models.TimeField(blank=True, null=True)
    works_day_and_night = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Pharmacy"
        verbose_name_plural = "Pharmacies"

    def __str__(self):
        return f"{self.name}"


class PharmacyMedicineManager(models.Manager):
    def get_pharmacy_and_medicine(self):
        return self.select_related("medicine", "pharmacy",
                                   "pharmacy__district").order_by("price")


class PharmacyMedicine(models.Model):
    pharmacy = models.ForeignKey(Pharmacy,
                                 on_delete=models.CASCADE,
                                 related_name="pharmacy_medicine" )
    medicine = models.ForeignKey(Medicine,
                                 on_delete=models.CASCADE,
                                 related_name="pharmacy_medicine")
    price = models.DecimalField(max_digits=13, decimal_places=2)
    available = models.BooleanField(default=True)
    objects = PharmacyMedicineManager()
