from django.db import models

class Album(models.Model):
    nome = models.CharField(max_length=20);
    artista = models.CharField(max_length=20, null=True); 
    lancamento = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2);
    
    def __str__(self):
        return self.nome;

class Loja(models.Model):
    nome = models.CharField(max_length=100);
    endereco = models.CharField(max_length=150);
    tel_para_contato = models.IntegerField(null=True)
    
    def __str__(self):
        return self.nome;

class Cliente(models.Model):
    nome = models.CharField(max_length=100);
    endereco_de_residencia = models.CharField(max_length=150);
    email = models.CharField(max_length=20, null=True); 
    
    def __str__(self):
        return self.nome;