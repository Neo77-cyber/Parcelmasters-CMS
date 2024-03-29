# Generated by Django 4.1.7 on 2023-05-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.IntegerField(blank=True, null=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('pickup_phone_number', models.IntegerField()),
                ('pickup_address', models.CharField(max_length=200)),
                ('recipient_name', models.CharField(max_length=200)),
                ('recipient_phone_number', models.IntegerField()),
                ('recipient_address', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('food', 'FOOD'), ('phones', 'PHONES'), ('computer accessories', 'COMPUTER ACCESSORIES'), ('miscellaneous', 'MISCELLANEOUS')], default='food', max_length=200)),
                ('status', models.CharField(blank=True, choices=[('awaiting payment', 'AWAITING PAYMENT'), ('consignment booked', 'CONSIGNMENT BOOKED'), (' delivery scheduled', 'DELIVERY SCHEDULED'), ('customs clearance', 'CUSTOMS CLEARANCE'), ('delay. temporary volume surge', 'DELAY. TEMPORARY VOLUME SURGE'), ('collected by customer at office', 'COLLECTED BY CUSTOMER AT OFFICE')], default='awaiting payment', max_length=100, null=True)),
            ],
        ),
    ]
