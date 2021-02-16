from django.contrib import admin
from .models import News, Category


# добавляем новые поля в таблицу для админки
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('category',)
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# регистрируем основную модель, изменения в админку
# важен порядок добавления - сначало регистрируем основную модель - потом класс по ее настройке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)