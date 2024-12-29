from django.db import migrations


def create_store_types(apps, schema_editor):
    StoreTypes = apps.get_model("stores", "StoreTypes")
    StoreTypes.objects.bulk_create([StoreTypes(name="salla"), StoreTypes(name="zid")])


def reverse_store_types(apps, schema_editor):
    StoreTypes = apps.get_model("stores", "StoreTypes")
    StoreTypes.objects.filter(name__in=["salla", "zid"]).delete()


class Migration(migrations.Migration):

    dependencies = [("stores", "0001_initial")]

    operations = [migrations.RunPython(create_store_types, reverse_store_types)]
