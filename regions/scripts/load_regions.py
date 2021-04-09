import csv
import os

from config.settings import BASE_DIR
from regions.models import Region, District


def insert_region_district():
    fhand = open(
        os.path.join(BASE_DIR, "regions/csv_data/region_district.csv"),
        encoding="utf8",
    )
    reader = csv.reader(fhand)
    header = next(reader)
    if header is not None:
        for row in reader:
            region, created = Region.objects.get_or_create(
                name=row[1],
            )
            district, created = District.objects.get_or_create(
                name=row[0], region=region
            )
            district.save()

        print("Successfully added")


def run():
    insert_region_district()
