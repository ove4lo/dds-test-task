from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Status, RecordType, Record, Category
from .serializers import StatusSerializer, RecordTypeSerializer, RecordSerializer, CategorySerializer

# ViewSet для управления статусами
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    # Удаление статуса
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.record_set.exists():
            return Response(
                {"error": "Нельзя удалить статус, который используется в записях"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

# ViewSet для управления типами записей
class RecordTypeViewSet(viewsets.ModelViewSet):
    queryset = RecordType.objects.all()
    serializer_class = RecordTypeSerializer

    # Удаление типа
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.record_set.exists():
            return Response(
                {"error": "Нельзя удалить тип, который используется в записях"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if instance.category_set.exists():
            return Response(
                {"error": "Нельзя удалить тип, который связан с категориями и подкатегориями"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

# ViewSet для управления категориями и подкатегориями
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Удаление категории
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.records.exists():
            return Response(
                {"error": "Нельзя удалить категорию, которая используется в записях"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

    # Получение подкатегории для данной категории
    @action(detail=True, methods=['get'])
    def subcategories(self, request, pk=None):
        category = self.get_object()
        subcategories = Category.objects.filter(parent_category=category)
        serializer = self.get_serializer(subcategories, many=True)
        return Response(serializer.data)

    # Получение категории по типу
    @action(detail=True, methods=['get'], url_path='by-type')
    def by_type(self, request, pk=None):
        queryset = self.get_queryset().filter(
            record_type_id=pk,
            parent_category__isnull=True
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# ViewSet для управления записями
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'record_date': ['exact', 'gte', 'lte'],  # Фильтрация по дате (диапазон)
        'status': ['exact'],
        'record_type': ['exact'],
        'category': ['exact'],
        'subcategory': ['exact'],
    }

    # Для фильтрации записи
    def get_queryset(self):
        return Record.objects.select_related('status', 'record_type', 'category', 'subcategory')