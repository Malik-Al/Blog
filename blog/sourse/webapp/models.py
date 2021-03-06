from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Розное'),
    ('food', 'Еда'),
    ('it', 'IT-сфера'),
    ('psycho', 'Психология'),
    ('bikers', 'Велосипеды'),
)


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')

    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')

    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')

    cotegory = models.CharField(max_length=20, verbose_name='Тема', default=CATEGORY_CHOICES[0][0],
                                choices=CATEGORY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)