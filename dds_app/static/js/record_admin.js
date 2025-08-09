(function($) {
    $(document).ready(function() {
        console.log("JavaScript loaded successfully");

        // Подсветка активных полей
        $('.form-row input, .form-row select, .form-row textarea').focus(function() {
            $(this).css('border-color', '#63b3ed');
        }).blur(function() {
            $(this).css('border-color', '#4a5568');
        });

        // Улучшение видимости placeholder
        $('input, textarea').each(function() {
            if ($(this).attr('placeholder')) {
                $(this).attr('placeholder', $(this).attr('placeholder')).css('color', '#a0aec0');
            }
        });

        // Динамическая фильтрация категорий и подкатегорий
        const recordTypeField = $('#id_record_type');
        const categoryField = $('#id_category');
        const subcategoryField = $('#id_subcategory');

        if (!recordTypeField.length || !categoryField.length || !subcategoryField.length) {
            console.error("One or more form fields not found:", {
                recordType: recordTypeField.length,
                category: categoryField.length,
                subcategory: subcategoryField.length
            });
            return;
        }

        // Обновление категорий при изменении типа
        recordTypeField.change(function() {
            const recordTypeId = $(this).val();
            console.log("Selected record type ID:", recordTypeId);
            if (recordTypeId) {
                $.get(`/categories/${recordTypeId}/by-type/`, function(data) {
                    console.log("Received categories:", data);
                    categoryField.empty().append('<option value="">---------</option>');
                    if (data.length > 0) {
                        $.each(data, function(index, item) {
                            categoryField.append(`<option value="${item.id}">${item.name}</option>`);
                        });
                    } else {
                        console.warn("No categories found for this type");
                    }
                    // Сбрасываем подкатегорию
                    subcategoryField.val('').empty().append('<option value="">---------</option>');
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    console.error("API request failed:", textStatus, errorThrown);
                });
            } else {
                categoryField.empty().append('<option value="">---------</option>');
                subcategoryField.empty().append('<option value="">---------</option>');
            }
        });

        // Обновление подкатегорий при изменении категории
        categoryField.change(function() {
            const categoryId = $(this).val();
            console.log("Selected category ID:", categoryId);
            if (categoryId) {
                $.get(`/categories/${categoryId}/subcategories/`, function(data) {
                    console.log("Received subcategories:", data);
                    subcategoryField.empty().append('<option value="">---------</option>');
                    if (data.length > 0) {
                        $.each(data, function(index, item) {
                            subcategoryField.append(`<option value="${item.id}">${item.name}</option>`);
                        });
                    } else {
                        console.warn("No subcategories found for this category");
                    }
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    console.error("API request failed:", textStatus, errorThrown);
                });
            } else {
                subcategoryField.empty().append('<option value="">---------</option>');
            }
        });

        // Валидация обязательных полей
        $('form').submit(function(e) {
            if (!recordTypeField.val()) {
                alert('Поле "Тип" обязательно для заполнения');
                e.preventDefault();
                return;
            }
            if (!categoryField.val()) {
                alert('Поле "Категория" обязательно для заполнения');
                e.preventDefault();
                return;
            }
            if (!subcategoryField.val()) {
                alert('Поле "Подкатегория" обязательно для заполнения');
                e.preventDefault();
                return;
            }
            if (!$('#id_amount').val() || $('#id_amount').val() <= 0) {
                alert('Поле "Сумма" должно быть больше 0');
                e.preventDefault();
                return;
            }
        });
    });
})(django.jQuery);