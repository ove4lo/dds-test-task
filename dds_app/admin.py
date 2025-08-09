from django.contrib import admin
from .models import Status, RecordType, Category, Record
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'actions_column')
    search_fields = ('name',)

    def actions_column(self, obj):
        edit_url = reverse('admin:dds_app_status_change', args=[obj.pk])
        delete_url = reverse('admin:dds_app_status_delete', args=[obj.pk])
        return format_html(
            f'<a href="{edit_url}" title="Редактировать" class="button"><i class="ri-edit-line"></i></a>'
            f'<a href="{delete_url}" title="Удалить" class="button"><i class="ri-delete-bin-line"></i></a>'
        )
    actions_column.short_description = 'Действия'

@admin.register(RecordType)
class RecordTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'actions_column')
    search_fields = ('name',)

    def actions_column(self, obj):
        edit_url = reverse('admin:dds_app_recordtype_change', args=[obj.pk])
        delete_url = reverse('admin:dds_app_recordtype_delete', args=[obj.pk])
        return format_html(
            f'<a href="{edit_url}" title="Редактировать" class="button"><i class="ri-edit-line"></i></a>'
            f'<a href="{delete_url}" title="Удалить" class="button"><i class="ri-delete-bin-line"></i></a>'
        )
    actions_column.short_description = 'Действия'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'record_type', 'view_subcategories', 'actions_column')
    list_filter = ('record_type', 'parent_category',)  # Кортеж
    search_fields = ('name',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(parent_category__isnull=True)

    def view_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        if subcategories:
            links = []
            for sub in subcategories:
                url = reverse('admin:dds_app_category_change', args=[sub.pk])
                link_html = f'<a href="{url}">{sub.name}</a>'
                links.append(link_html)
            return format_html("<br>".join(links))
        return "-"
    view_subcategories.short_description = 'Подкатегории'

    def actions_column(self, obj):
        edit_url = reverse('admin:dds_app_category_change', args=[obj.pk])
        delete_url = reverse('admin:dds_app_category_delete', args=[obj.pk])
        add_url = reverse('admin:dds_app_category_add') + f'?parent_category={obj.pk}'
        return format_html(
            f'<a href="{edit_url}" title="Редактировать" class="button"><i class="ri-edit-line"></i></a>'
            f'<a href="{delete_url}" title="Удалить" class="button"><i class="ri-delete-bin-line"></i></a>'
            f'<a href="{add_url}" title="Добавить подкатегорию" class="button"><i class="ri-add-line"></i></a>'
        )
    actions_column.short_description = 'Действия'

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "record_date",
        "status",
        "record_type",
        "category",
        "subcategory",
        "amount",
        "actions_column",
    )
    list_filter = (
        "record_date",
        "status",
        "record_type",
        "category",
        "subcategory",
    )
    search_fields = ("comment",)  # Кортеж

    fieldsets = (
        ('Основная информация', {
            'fields': ('record_date', 'status', 'record_type')
        }),
        ('Категории', {
            'fields': ('category', 'subcategory')
        }),
        ('Финансовые данные', {
            'fields': ('amount',)
        }),
        ('Дополнительно', {
            'fields': ('comment',)
        }),
    )

    autocomplete_fields = ['status', 'record_type', 'category', 'subcategory']

    class Media:
        css = {
            'all': ('dds_app/css/record_admin.css',)
        }
        js = (
            'dds_app/js/record_admin.js',
        )

    def actions_column(self, obj):
        edit_url = reverse('admin:dds_app_record_change', args=[obj.pk])
        delete_url = reverse('admin:dds_app_record_delete', args=[obj.pk])
        return format_html(
            f'<a href="{edit_url}" title="Редактировать" class="button"><i class="ri-edit-line"></i></a>'
            f'<a href="{delete_url}" title="Удалить" class="button"><i class="ri-delete-bin-line"></i></a>'
        )
    actions_column.short_description = 'Действия'