from django.db import models
from django.contrib.auth import get_user_model

from apps.store.models.manuals_models import Product, Counterparty, Delivery

User = get_user_model()


class Movement(models.Model):
    """ Поставка | Отгрузка товаров """

    class Types(models.TextChoices):
        SUPPLY = 'SU', 'Поставка'
        SHIPMENT = 'SH', 'Отгрузка'

    move_type = models.CharField(choices=Types.choices, max_length=2, verbose_name='Тип движения',
                                 help_text='Поставка / Отгрузка')

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='supplies', verbose_name='Пользователь')

    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT, related_name='supplies',
                                 verbose_name='Способ доставки')

    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Движения'
        verbose_name_plural = 'Движение'

    def __str__(self):
        return f'{self.move_type} {self.id} - {self.created}'


class StrProduct(models.Model):
    """ Строка товара, дополненительная таблица к поставке / отгрузке """

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='receipts', verbose_name='Товар')
    counterparty = models.ForeignKey(Counterparty, on_delete=models.PROTECT, related_name='receipts',
                                     verbose_name='Контрагент')
    supply = models.ForeignKey(Movement, on_delete=models.PROTECT, related_name='receipts', verbose_name='Поставка')

    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена закупки', default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        ordering = ('product',)
        verbose_name = 'Строки товаров'
        verbose_name_plural = 'Строка товара'

    def __str__(self):
        return f'Строка товара {self.id}: {self.product}, {self.quantity} ед.'
