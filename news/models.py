from django.db import models


class News (models.Model):
    title= models.CharField(max_length=200, verbose_name='Оглавление')
    content =models.TextField(verbose_name="Текст новости")
    created_new=models.DateTimeField(auto_now_add=True, verbose_name="Время создания новости")
    updated_new=models.DateTimeField(auto_now=True, verbose_name="Время последнего редактирования")
    photo=models.ImageField(upload_to='NewPhoto/%Y/%m/%d')
    published=models.BooleanField (default=False, verbose_name="Опубликованно")
    category=models.ForeignKey('Category',on_delete=models.PROTECT, verbose_name='Категории',null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['-created_new']

class Category (models.Model):
    title=models.CharField(max_length=200, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']