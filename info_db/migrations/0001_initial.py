# Generated by Django 2.1.5 on 2021-11-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioLang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfoNoAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('e_mail', models.EmailField(max_length=254)),
                ('e_mail_optional', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RepertoirePieceChamber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composer', models.CharField(max_length=100)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RepertoirePieceOrchestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composer', models.CharField(max_length=100)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RepertoirePieceSolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composer', models.CharField(max_length=100)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RepertoirePieceWPiano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composer', models.CharField(max_length=100)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
