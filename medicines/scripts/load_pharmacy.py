import csv
import os
import random

from config.settings import BASE_DIR
from medicines.models import Pharmacy
from regions.models import District


def insert_pharmacies():
    fhand = open(
        os.path.join(BASE_DIR, "medicines/csv_data/pharmacy_list.csv"),
        encoding="utf8",
    )
    reader = csv.reader(fhand)
    header = next(reader)
    pharmacies_instances = []
    districts = District.objects.all()
    if header is not None:
        for row in reader:
            pharmacy = Pharmacy(name=row[0],
                                phone_number=row[1],
                                address='',
                                works_day_and_night=random.choice(
                                    [True, False]),
                                district=random.choice(districts))
            pharmacies_instances.append(pharmacy)
        Pharmacy.objects.bulk_create(pharmacies_instances)
        print("Successfully added")

def run():
    insert_pharmacies()
