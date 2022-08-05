# Generated by Django 4.1 on 2022-08-05 07:10

import django
from django.db import migrations


def is_postgresql(schema_editor):
    return schema_editor.connection.vendor == "postgresql"


def get_db_table(apps):
    ResetPasswordToken = apps.get_model(
        "django_rest_passwordreset", "ResetPasswordToken"
    )
    db_table = ResetPasswordToken._meta.db_table
    return db_table


def execute_sql(schema_editor, sql):
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(sql)


def forwards_func(apps, schema_editor):
    if not is_postgresql(schema_editor):
        return

    db_table = get_db_table(apps)
    sql = """alter table {db_table}
    alter column id add generated by default as identity;
    """.format(db_table=db_table)

    execute_sql(schema_editor, sql)


def reverse_func(apps, schema_editor):
    if not is_postgresql(schema_editor):
        return

    db_table = get_db_table(apps)
    sql = """alter table {db_table}
    alter column id drop identity;
    """.format(db_table=db_table)

    execute_sql(schema_editor, sql)


def get_migrations_based_on_django_version():
    django_version = django.VERSION

    if ((django_version[0] == 4 and django_version[1] >= 1) or
        django_version[0] >= 5):
        return [
            migrations.RunPython(forwards_func, reverse_code=reverse_func),
        ]

    return []


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_passwordreset', '0003_allow_blank_and_null_fields'),
    ]

    operations = get_migrations_based_on_django_version()
