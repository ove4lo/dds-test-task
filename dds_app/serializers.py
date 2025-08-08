from rest_framework import serializers
from .models import Status, RecordType, Record, Category
from django.core.validators import MinValueValidator

# Сериализатор класса "Статус"
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

# Сериализатор класса "Статус"
class RecordTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordType
        fields = '__all__'

# Сериализатор класса "Категория"
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # Метод валдации
    def validate(self, data):
        parent = data.get('parent_category')
        record_type = data.get('record_type')

        # Подкатегория не может существовать без категории
        if not parent and record_type:
            raise serializers.ValidationError(
                {"parent_category": "Подкатегория должна иметь родительскую категорию."}
            )

        # Категория должна иметь тип
        if parent and not record_type:
            raise serializers.ValidationError(
                {"record_type": "Категория должна иметь тип."}
            )

        return data

# Сериализатор класса "Запись"
class RecordSerializer(serializers.ModelSerializer):
    # Связанные поля обязательные
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        required=True
    )
    record_type = serializers.PrimaryKeyRelatedField(
        queryset=RecordType.objects.all(),
        required=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(parent_category__isnull=True),
        required=True
    )
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(parent_category__isnull=False),
        required=True
    )

    # Сумма должна быть положительная
    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        required=True
    )

    class Meta:
        model = Record
        fields = '__all__'

    # Метод валидации
    def validate(self, data):
        category = data.get('category')
        subcategory = data.get('subcategory')
        record_type = data.get('record_type')

        if category.record_type != record_type:
            raise serializers.ValidationError(
                {"category": "Категория не принадлежит выбранному типу."}
            )

        if subcategory.parent_category != category:
            raise serializers.ValidationError(
                {"subcategory": "Подкатегория не принадлежит выбранной категории."}
            )

        return data