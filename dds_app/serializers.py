from rest_framework import serializers
from .models import Status, RecordType, Record, Category

# Сериализатор класса "Статус"
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = 'all'

# Сериализатор класса "Статус"
class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = 'all'

# Сериализатор класса "Категория"
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'

# Сериализатор класса "Запись"
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['amount', 'record_type', 'category', 'subcategory', 'comment', 'record_date', 'created_at']

    # Метод для валидации бизнес-правил
    def validate(self, data):
        record_type = data.get('record_type')
        category = data.get('category')
        subcategory = data.get('subcategory')

        # 1. Проверка, что категория принадлежит данному типу
        if category and record_type:
            if category.record_type != record_type:
                raise serializers.ValidationError(
                    {"category": "Выбранная категория не соответствует типу записи."}
                )

        # 2. Проверка, что данная подкатегория принадлежит данной категории
        if subcategory and category:
            # Убеждаемся, что подкатегория действительно является дочерней для категории
            if subcategory.parent_category != category:
                raise serializers.ValidationError(
                    {"subcategory": "Выбранная подкатегория не принадлежит к выбранной категории."}
                )

        # Проверка, что subcategory является подкатегорией
        if subcategory and not subcategory.is_subcategory():
            raise serializers.ValidationError(
                {"subcategory": "Поле 'subcategory' должно быть подкатегорией."}
            )

        return data