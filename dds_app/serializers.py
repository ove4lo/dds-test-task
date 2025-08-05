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
    status = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        required=True,
        slug_field='name',
        error_messages={"null": "Поле 'status' обязательно."}
    )
    record_type = serializers.PrimaryKeyRelatedField(
        queryset=RecordType.objects.all(),
        required=True,
        slug_field='name',
        error_messages={"null": "Поле 'record_type' обязательно."}
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(parent_category__isnull=True),
        required=True,
        slug_field='name',
        error_messages={"null": "Поле 'category' обязательно."}
    )
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True,
        slug_field='name',
        error_messages={"null": "Поле 'subcategory' обязательно."}
    )
    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        error_messages={"null": "Поле 'amount' обязательно."}
    )
    comment = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
    record_date = serializers.DateField(
        required=True,
        error_messages={"null": "Поле 'record_date' обязательно."}
    )
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Record
        fields = ['amount', 'status', 'record_type', 'category', 'subcategory', 'comment', 'record_date', 'created_at']

    # Метод для валидации бизнес-правил
    def validate(self, data):
        status = data.get('status')
        record_type = data.get('record_type')
        category = data.get('category')
        subcategory = data.get('subcategory')

        # 1. Проверка, что данная категория принадлежит данному типу
        if category and record_type and category.record_type != record_type:
            raise serializers.ValidationError(
                {"category": "Выбранная категория не соответствует типу записи."}
            )

        # 2. Проверка, что данная подкатегория принадлежит данной категории
        if subcategory and category and subcategory.parent_category != category:
            raise serializers.ValidationError(
                {"subcategory": "Выбранная подкатегория не принадлежит к выбранной категории."}
            )

        # 3. Проверка, что subcategory является подкатегорией
        if subcategory and not subcategory.is_subcategory():
            raise serializers.ValidationError(
                {"subcategory": "Поле 'subcategory' должно быть подкатегорией."}
            )

        return data