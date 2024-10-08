# Generated by Django 4.2 on 2024-08-16 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="status",
            field=models.BooleanField(
                choices=[(False, "Не проверено"), (True, "Проверено")],
                db_column="Status",
                default=0,
                verbose_name="Проверено",
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="adds",
            field=models.IntegerField(
                db_column="Favorites", default=0, verbose_name="В избранном"
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="answer",
            field=models.TextField(
                db_column="Answer", max_length=5000, verbose_name="Ответ"
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="category",
            field=models.ForeignKey(
                db_column="CategoryID",
                on_delete=django.db.models.deletion.CASCADE,
                to="cards.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="question",
            field=models.CharField(
                db_column="Question", max_length=255, verbose_name="Вопрос"
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="upload_date",
            field=models.DateTimeField(
                auto_now_add=True, db_column="UploadDate", verbose_name="Дата загрузки"
            ),
        ),
        migrations.AlterField(
            model_name="card",
            name="views",
            field=models.IntegerField(
                db_column="Views", default=0, verbose_name="Просмотры"
            ),
        ),
    ]
