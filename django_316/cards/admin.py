# from typing import Any
from django.contrib import admin
# from django.db.models.query import QuerySet
from .models import Card
from django.contrib.admin import SimpleListFilter


class CardCodeFilter(SimpleListFilter):
    title = 'Наличие кода'
    parameter_name = 'has_code'


    def lookups(self, request, model_admin):
        return (
            ('yes', 'Да'),
            ('no', 'Нет')
        )
    

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(answer__contains='```')
        elif self.value() == 'no':
            return queryset.exclude(answer__contains='```')



@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    # поля которые будут отображаться в админке
    list_display = ('pk', 'question', 'category', 'views', 'upload_date', 'status', 'brief_info',)
    # поля которые будут ссылками
    list_display_links = ('pk', 'upload_date',)
    # поля по которым можно проводить поиск
    search_fields = ('answer',)
    # поля по которым мы можем проводить филльтрацию
    list_filter = ('category', 'status', CardCodeFilter)
    # сортировка по полям
    ordering = ('-views', 'category',)
    # изменение выводимого количества элементов на страницу
    list_per_page = 12
    # поля которые можно редактировать напрямую
    list_editable = ('views', 'question', 'status',)

    actions = ['set_checked', 'set_unchecked']

    @admin.action(description='Пометить как проверенные')
    def set_checked(self, request, queryset):
        updated_count = queryset.update(status=Card.Status.CHECKED)
        self.message_user(request, f'{updated_count} записей было помечено как проверенные', 'info')

    @admin.action(description='Пометить как не проверенные')
    def set_unchecked(self, request, queryset):
        updated_count = queryset.update(status=Card.Status.UNCHECKED)
        self.message_user(request, f'{updated_count} записей было помечено как не проверенные', 'warning')

    # определение метода для отображения краткой информации в карточке
    @admin.display(description='Наличие кода', ordering='answer')
    def brief_info(self, card):
        has_code = 'Да' if '```' in card.answer else 'Нет'
        return has_code
    

    
# сначала задаётся класс, который добавляет модель в админку
# потом этот класс связывается с админкой через admin.site.register()
# либо сразу через декоратор @admin.register(Card)
# admin.site.register(Card, CardAdmin)