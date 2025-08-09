from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Модель статуса
class Status(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Название"))

    class Meta:
        verbose_name = _("Статус")
        verbose_name_plural = _("Статусы")

    def __str__(self):
        return self.name

# Модель типа
class RecordType(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_("Название"))

    class Meta:
        verbose_name = _("Тип")
        verbose_name_plural = _("Типы")

    def __str__(self):
        return self.name

# Модель категории и подкатегории
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name=_("Название"))
    record_type = models.ForeignKey(
        RecordType,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Тип")
    )
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name = _("Родительская категория")
    )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        if self.parent_category:
            return f" {self.name}"
        return self.name

    def is_subcategory(self):
        return self.parent_category is not None

# Модель записи
class Record(models.Model):
    record_date = models.DateField(default=timezone.now, verbose_name=_("Дата записи"))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=False,
        verbose_name=_("Статус")
    )
    record_type = models.ForeignKey(
        RecordType,
        on_delete=models.PROTECT,
        null=False,
        verbose_name=_("Тип записи")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        limit_choices_to={'parent_category__isnull': True},
        related_name='records',
        verbose_name=_("Категория")
    )
    subcategory = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='sub_records',
        limit_choices_to={'parent_category__isnull': False},
        verbose_name=_("Подкатегория")
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Сумма"))
    comment = models.TextField(blank=True, null=True, verbose_name=_("Комментарий"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    class Meta:
        verbose_name = _("Запись")
        verbose_name_plural = _("Записи")

    def __str__(self):
        parts = [
            f"Запись от {self.record_date} ({self.amount} руб.)"
        ]

        if self.category:
            parts.append(f"Категория: {self.category.name}")

        if self.subcategory:
            parts.append(f"Подкатегория: {self.subcategory.name}")

        return ", ".join(parts)