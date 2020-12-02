from django.contrib import admin

from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','created_new','updated_new','published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_filter = ('category', 'published')
    list_editable = ('published',)


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ('title',)

admin.site.register (News,NewsAdmin)
admin.site.register (Category,CategoryAdmin)