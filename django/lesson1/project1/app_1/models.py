from django.db import models


class Mebel(models.Model):
    link = models.TextField('Ссылка')
    price = models.DecimalField(decimal_places=10, max_digits=10)
    description = models.TextField('Описание')

