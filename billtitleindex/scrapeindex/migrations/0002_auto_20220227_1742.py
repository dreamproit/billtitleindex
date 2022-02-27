# Generated by Django 3.2.12 on 2022-02-27 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapeindex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billstagetitle',
            name='bill_basic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billstagetitle', to='scrapeindex.billbasic', verbose_name='bill basic'),
        ),
        migrations.AlterField(
            model_name='billtitles',
            name='bill_basic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billtitles', to='scrapeindex.billbasic', verbose_name='bill basic'),
        ),
    ]
