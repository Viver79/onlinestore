# Generated by Django 3.1.5 on 2021-02-26 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210218_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='bike',
        ),
    ]