from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from dds_app.models import Status, RecordType, Category, Record
from django.utils import timezone

class Command(BaseCommand):
    help = 'Инициализирует базу данных тестовыми данными и создает суперпользователя'

    def handle(self, *args, **kwargs):
        # Создание статусов
        statuses = ['Бизнес', 'Личное', 'Налог']
        for status_name in statuses:
            Status.objects.get_or_create(name=status_name)
        self.stdout.write(self.style.SUCCESS('Статусы успешно созданы'))

        # Создание типов записей
        record_types = ['Пополнение', 'Списание']
        for type_name in record_types:
            RecordType.objects.get_or_create(name=type_name)
        self.stdout.write(self.style.SUCCESS('Типы записей успешно созданы'))

        # Создание категорий и подкатегорий
        categories = [
            {
                'name': 'Инфраструктура',
                'record_type': 'Списание',
                'subcategories': ['VPS', 'Proxy']
            },
            {
                'name': 'Маркетинг',
                'record_type': 'Списание',
                'subcategories': ['Farpost', 'Avito']
            }
        ]

        for cat in categories:
            record_type = RecordType.objects.get(name=cat['record_type'])
            parent_category, _ = Category.objects.get_or_create(
                name=cat['name'],
                record_type=record_type,
                parent_category=None
            )
            for subcat_name in cat['subcategories']:
                Category.objects.get_or_create(
                    name=subcat_name,
                    record_type=record_type,
                    parent_category=parent_category
                )
        self.stdout.write(self.style.SUCCESS('Категории и подкатегории успешно созданы'))

        # Создание тестовых записей
        statuses = Status.objects.all()
        record_types = RecordType.objects.all()
        categories = Category.objects.filter(parent_category__isnull=True)
        subcategories = Category.objects.filter(parent_category__isnull=False)

        for i in range(10):
            record = Record.objects.create(
                record_date=timezone.now(),
                status=statuses[i % len(statuses)],  # Рандомный статус
                record_type=record_types[i % len(record_types)],  # Рандомный тип
                category=categories[i % len(categories)],  # Рандомная категория
                subcategory=subcategories[i % len(subcategories)],  # Рандомная подкатегория
                amount=(i + 1) * 100.00,  # Рандомная сумма
                comment=f"Тестовая запись #{i + 1}"
            )
        self.stdout.write(self.style.SUCCESS('Тестовые записи успешно созданы'))

        # Создание суперпользователя
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан: admin/admin123'))
        else:
            self.stdout.write(self.style.WARNING('Суперпользователь уже существует'))