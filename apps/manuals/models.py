import uuid

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField


class Manual(models.Model):
    """ Абстрактная модель для справочников """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='Наименование', max_length=100)
    slug = models.SlugField(verbose_name='SLUG', max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ('title',)

    def __str__(self):
        return self.title


class Category(MPTTModel, Manual):
    """ Справочник категорий """

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True,
                            related_name='children', verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


class Units(Manual):
    """ Справочник единиц измерений """

    class Meta:
        verbose_name = 'Единицы измерения'
        verbose_name_plural = 'Единица измерения'


class Brand(Manual):
    """ Справочник брендов """

    class Meta:
        verbose_name = 'Бренды'
        verbose_name_plural = 'Бренд'


class Counterparty(Manual):
    """ Справочник контрагентов """

    phone = PhoneNumberField(verbose_name='Номер телефона', blank=True, null=True)
    email = models.EmailField(verbose_name='E-Mail', blank=True, null=True)
    link = models.URLField(verbose_name='Ссылка', blank=True, null=True)

    class Meta:
        verbose_name = 'Контрагенты'
        verbose_name_plural = 'Контрагент'


class Delivery(Manual):
    """ Справочник способов доставки"""

    class Meta:
        verbose_name = 'Способы доставки'
        verbose_name_plural = 'Способ доставки'


class Product(Manual):
    """ Справочник товаров """

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд', related_name='products')
    unit = models.ForeignKey(Units, on_delete=models.PROTECT, verbose_name='Ед.изм.', related_name='products')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='products')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'
