# Generated by Django 4.2.7 on 2023-11-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Recognation', '0003_face_recognation2_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face_recognation2',
            name='image',
            field=models.ImageField(default=None, upload_to='./media_image'),
        ),
    ]
