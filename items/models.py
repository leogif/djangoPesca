from django.db import models

# Create your models here.
class Pesca(models.Model):
	nome = models.CharField(max_length=200)
	preco = models.DecimalField(max_digits=5,decimal_places=2)
	descricao = models.TextField()

	def __str__(self):
		return self.nome