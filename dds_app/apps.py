from django.apps import AppConfig

class DdsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dds_app'

    def ready(self):
        from django.contrib import admin
        admin.site.site_header = "ДДС Панель управления"
        admin.site.site_title = "ДДС Портал"
        admin.site.index_title = "Добро пожаловать в админ-панель ДДС"