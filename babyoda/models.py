from django.db import models

# Create your models here.

class Lista(models.Model):
    item = models.CharField(max_length=200)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='chaFraldas')

    def __str__(self):
        return self.item

class Mensagens(models.Model):
    nome = models.CharField(max_length=255)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    

class Galeria(models.Model):
    info_foto = models.CharField(max_length=255)
    slug = models.ImageField(upload_to='galeria')
    foto = models.ImageField(upload_to='galeria')

    def __str__(self):
        return self.info_foto
    
