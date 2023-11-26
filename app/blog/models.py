from autor.models import Autor
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["nome"]


class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to="postagens", null=True, blank=True)
    slug = models.SlugField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-data_publicacao"]
        verbose_name_plural = "Postagens"
