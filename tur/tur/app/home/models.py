from django.db import models

# Create your models here.

class Clients(models.Model):
    имя = models.CharField('Имя',max_length=25)
    телефон = models.CharField('Телефон',max_length=13)
    e_mail = models.CharField('E-mail',max_length=25)
    текст = models.CharField('Сообщение',max_length=300)

    def __str__(self):
        return self.имя
