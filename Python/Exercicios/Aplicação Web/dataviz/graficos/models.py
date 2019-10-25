from django.db import models
from django.forms import ModelForm

# Create your models here.

class Grafico(models.Model):
    tipo = models.CharField(max_length=16, choices=[('l','linha'),('b','barra')])
    dadosx = models.CharField(max_length=1000,null=False)
    dadosy = models.CharField(max_length=1000,null=False)

class FormularioDoGrafico(ModelForm):
    class Meta:
        model = Grafico
        fields = ['tipo', 'dadosx', 'dadosy']
        labels = {
            'tipo': 'Tipo',
            'dadosx': "valores de x",
            'dadosy': "valores de y"
        }
        # help_texts = {
        #     'tipo': 'Escolha o tipo do gráfico',
        #     'dadosx': 'Entre com os valores de x'
        # }
        # error_messages = {
        #     'tipo': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }