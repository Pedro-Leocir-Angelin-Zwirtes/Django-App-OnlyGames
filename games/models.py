from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    url_foto = models.CharField(max_length=1000)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
