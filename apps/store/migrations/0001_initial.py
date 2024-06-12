# Generated by Django 5.0.6 on 2024-06-12 22:10

import django.db.models.deletion
import mptt.fields
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Бренды',
                'verbose_name_plural': 'Бренд',
            },
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Mail')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Контрагенты',
                'verbose_name_plural': 'Контрагент',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Способы доставки',
                'verbose_name_plural': 'Способ доставки',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Единицы измерения',
                'verbose_name_plural': 'Единица измерения',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_type', models.CharField(choices=[('SU', 'Поставка'), ('SH', 'Отгрузка')], help_text='Поставка / Отгрузка', max_length=2, verbose_name='Тип движения')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplies', to='store.delivery', verbose_name='Способ доставки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplies', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Движения',
                'verbose_name_plural': 'Движение',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='SLUG')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.brand', verbose_name='Бренд')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.category', verbose_name='Категория')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.units', verbose_name='Ед.изм.')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='StrProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена закупки')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('counterparty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='store.counterparty', verbose_name='Контрагент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='store.product', verbose_name='Товар')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='store.movement', verbose_name='Поставка')),
            ],
            options={
                'verbose_name': 'Строки товаров',
                'verbose_name_plural': 'Строка товара',
                'ordering': ('product',),
            },
        ),
    ]