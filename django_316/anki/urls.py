from django.contrib import admin
from django.urls import path, include
from anki import settings
from cards import views

admin.site.site_header = 'Управление сайтом Anki'
admin.site.site_title = 'Админ.панель для Anki'
admin.site.index_title = 'Добро пожаловать в панель управления!'


# Подключаем файл urls.py из приложения cards через include
urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),
    # Маршруты для меню
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Маршруты подключенные из приложения cards
    path('cards/', include('cards.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # другие URL-паттерны 
    ] + urlpatterns