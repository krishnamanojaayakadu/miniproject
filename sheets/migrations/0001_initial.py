# Generated by Django 2.2 on 2020-10-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id1', models.CharField(max_length=100)),
                ('Centercode', models.CharField(max_length=100)),
                ('Centername', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
                ('Optioncode', models.CharField(max_length=100)),
                ('CourseName', models.CharField(max_length=100)),
                ('ExamDate', models.CharField(max_length=100)),
                ('Year', models.CharField(max_length=100)),
                ('ExamType', models.CharField(max_length=100)),
                ('HTNO', models.CharField(max_length=100)),
                ('CollCode', models.CharField(max_length=100)),
                ('SName', models.CharField(max_length=100)),
                ('Medium', models.CharField(max_length=100)),
                ('ExamMonthyear', models.CharField(max_length=100)),
                ('SubjectCode', models.CharField(max_length=100)),
                ('SubjectName', models.CharField(max_length=100)),
                ('SubjectType', models.CharField(max_length=100)),
                ('QPaperCode', models.CharField(max_length=100)),
                ('AnsBk', models.CharField(max_length=100)),
                ('Barcode', models.CharField(max_length=100)),
                ('BookletType', models.CharField(max_length=100)),
                ('IsAdditional', models.CharField(max_length=100)),
                ('IsBuffer', models.CharField(max_length=100)),
                ('OldBarcode', models.CharField(max_length=100)),
                ('OldAnsbk', models.CharField(max_length=100)),
                ('IsLocked', models.CharField(max_length=100)),
                ('Attstatus', models.CharField(max_length=100)),
                ('PackingSlip', models.CharField(max_length=100)),
                ('Pageno', models.CharField(max_length=100)),
                ('Pagerecslno', models.CharField(max_length=100)),
            ],
        ),
    ]
