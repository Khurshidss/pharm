# Generated by Django 3.1.5 on 2021-01-29 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0003_auto_20210129_0316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pharmacy',
            options={'verbose_name': 'Pharmacy', 'verbose_name_plural': 'Pharmacies'},
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='price',
        ),
        migrations.CreateModel(
            name='PharmacyMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_medicine', to='medicines.medicine')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_medicine', to='medicines.pharmacy')),
            ],
        ),
    ]
