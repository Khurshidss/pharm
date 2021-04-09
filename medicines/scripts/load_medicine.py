import csv
import os
import random

from config.settings import BASE_DIR
from medicines.models import Medicine


def insert_medicines():
    fhand = open(
        os.path.join(BASE_DIR, "medicines/csv_data/medicine_list.csv"),
        encoding="utf8",
    )
    reader = csv.reader(fhand)
    header = next(reader)
    medicines_instances = []
    manufacturers = ["Lupin Pharmaceuticals", "Sun Pharmaceuticals",
                     "Sandoz", "Mylan NV", "Teva "
                                           "Pharmaceutical Industries Ltd"]
    description = """
        Lorem Ipsum is simply dummy text of the printing and typesetting 
        industry. Lorem Ipsum has been the industry's standard dummy text ever 
        since the 1500s, when an unknown printer took a galley of type and 
        scrambled it to make a type specimen book. It has survived not only 
        five centuries, but also the leap into electronic typesetting, 
        remaining essentially unchanged. It was popularised in the 1960s 
        with the release of Letraset sheets containing Lorem Ipsum passages, 
        and more recently with desktop publishing software like Aldus 
        PageMaker including versions of Lorem Ipsum.
    """
    if header is not None:
        for row in reader:
            medicine = Medicine(barcode=row[0], title=row[1],
                                manufacturer=random.choice(manufacturers),
                                description=description,
                                medicine_type=random.choice(
                                    Medicine.MedicineType.values))
            medicines_instances.append(medicine)
        Medicine.objects.bulk_create(medicines_instances)
        print("Successfully added")


def run():
    insert_medicines()
