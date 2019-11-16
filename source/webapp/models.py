from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    desctiption= models.TextField(max_length=3000,null=True, blank=True, verbose_name='Описание' )
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

REVIEW_CHOICES = (
    (5, 'отлично'),
    (4, 'хорошо'),
    (3, 'удовлетворительно'),
    (2, 'плохо'),
    (1, 'отвратительно')
)

class Review(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='review',
                                on_delete=models.CASCADE, verbose_name='Товар')
    author = models.ForeignKey(User, null=True, blank=True, default=None, verbose_name='Автор',
                               on_delete=models.CASCADE, related_name='review')
    text = models.TextField(max_length=400, verbose_name='Текст отзыва')
    models.IntegerField(choices=REVIEW_CHOICES, verbose_name='Оценка')
