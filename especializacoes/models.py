from django.db import models

class Especializacoes(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField("")
    instituicao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'especializacoes'

    def __str__(self):
        return self.nome