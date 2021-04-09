import random

from medicines.models import Medicine, Pharmacy, PharmacyMedicine


def insert_pharmacy_medicine():
    medicines = Medicine.objects.all()
    pharmacies = Pharmacy.objects.all()
    pharmacy_len = len(pharmacies)
    pharmacy_medicine_instances = []
    for medicine in medicines:
        price = random.randint(1, 11) * 10000
        for i in range(1, random.randint(1, pharmacy_len)):
            pharmacy = random.choice(pharmacies)
            price = price + random.randint(1, 9) * 500
            pharmacy_medicine = PharmacyMedicine(medicine=medicine,
                                                 pharmacy=pharmacy,
                                                 price=price)
            pharmacy_medicine_instances.append(pharmacy_medicine)

    PharmacyMedicine.objects.bulk_create(pharmacy_medicine_instances)
    print("Successfully added")


def run():
    insert_pharmacy_medicine()
