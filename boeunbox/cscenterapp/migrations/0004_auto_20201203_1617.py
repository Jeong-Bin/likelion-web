# Generated by Django 3.1.2 on 2020-12-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cscenterapp', '0003_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQ',
            new_name='QNA',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='faq',
            new_name='qna',
        ),
    ]
