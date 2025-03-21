# Generated by Django 4.1.7 on 2023-04-13 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crystal_admin", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="addon_services",
            name="addon_images_url",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="decoration",
            name="decoration_images_url",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="food",
            name="food_images_url",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="addon_name",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="decoration_theam",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="addon_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="crystal_admin.addon_services",
            ),
        ),
        migrations.AddField(
            model_name="order_items",
            name="addon_name",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="addon_price",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="decoration_price",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="decoration_theam",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="food_item_name",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="order_items",
            name="suggestion",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="amobile_no",
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name="addon_services",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="addon_services",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="agent_commission",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="bank_details",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="bank_details",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="decoration",
            name="decoration_price",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="event_details",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="event_details",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="manager_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="crystal_admin.manager",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="order_items",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order_items",
            name="food_price",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="order_items",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order_services",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order_services",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="mobile_no",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="user",
            name="mobile_verified",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="contact",
            fields=[
                ("contact_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, null=True)),
                ("email", models.CharField(max_length=20, null=True)),
                ("msg", models.CharField(max_length=200, null=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crystal_admin.user",
                    ),
                ),
            ],
            options={
                "db_table": "contact",
            },
        ),
    ]
