from django.db import models

STATUS_CHOISES = [
        ('new', 'new'),
        ('in_progress', 'in progress'),
        ('done', 'done'),
    ]

class Task(models.Model):
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Текст')
    specific = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20,null=False, blank=False, choices=STATUS_CHOISES, default='new', verbose_name='Статус')
    date_of_completion = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return self.description
