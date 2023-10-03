from django.contrib.auth.models import User
from django.db import models


class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

    class Meta:
        verbose_name_plural = "Autores"
