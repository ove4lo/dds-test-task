from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusViewSet, RecordTypeViewSet, CategoryViewSet, RecordViewSet

# Роутер для автоматической генерации маршрутов
router = DefaultRouter()
router.register(r'statuses', StatusViewSet)
router.register(r'record-types', RecordTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]