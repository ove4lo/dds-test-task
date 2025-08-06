from django.db import models
from django.utils import timezone

# Модель статуса
class Status(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

# Модель типа
class RecordType(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

# Модель категории и подкатегории
class Category(models.Model):
    name = models.CharField(max_length=250)
    record_type = models.ForeignKey(
        RecordType,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    def __str__(self):
        if self.parent_category:
            return f"{self.parent_category.name}: {self.name}"
        return self.name

    def is_subcategory(self):
        return self.parent_category is not None

# Модель записи
class Record(models.Model):
    record_date = models.DateField(default=timezone.now)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=False
    )
    record_type = models.ForeignKey(
        RecordType,
        on_delete=models.PROTECT,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        limit_choices_to={'parent_category__isnull': True},
        related_name='records'
    )
    subcategory = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='sub_records',
        limit_choices_to={'parent_category__isnull': False}
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        parts = [
            f"Запись от {self.record_date} ({self.amount} руб.)"
        ]

        if self.category:
            parts.append(f"Категория: {self.category.name}")

        if self.subcategory:
            parts.append(f"Подкатегория: {self.subcategory.name}")

        return ", ".join(parts)