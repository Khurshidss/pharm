from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"


class DistrictManager(models.Manager):
    def filter_by_region(self, region_id):
        return self.filter(region_id=region_id)


class District(models.Model):
    name = models.CharField(max_length=512)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="districts",
    )
    objects = DistrictManager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-id']

