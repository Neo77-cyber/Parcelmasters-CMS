# Generated by Django 3.0.14 on 2023-02-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelcourier', '0002_shippingdetails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetails',
            name='Departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='pickup_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='status',
            field=models.CharField(blank=True, choices=[('awaiting payment', 'AWAITING PAYMENT'), ('consignment booked', 'CONSIGNMENT BOOKED'), (' delivery scheduled', 'DELIVERY SCHEDULED'), ('customs clearance', 'CUSTOMS CLEARANCE'), ('delay. temporary volume surge', 'DELAY. TEMPORARY VOLUME SURGE'), ('collected by customer at office', 'COLLECTED BY CUSTOMER AT OFFICE')], default='awaiting payment', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='tracking_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
