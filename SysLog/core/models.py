from django.db import models

class Cliente(models.Model):
    razao_social = models.CharField('Razão social', max_length=60)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=60)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=20)
    rg_inscricao_estadual = models.CharField('RG/Incrição Estadual', max_length=20, blank=True)
    data_nascimento = models.DateField('Data de Nascimento')
    uf = models.CharField('UF', max_length=25)
    cep = models.CharField('Cep', max_length=11)
    cidade = models.CharField('Cidade', max_length=30)
    bairro = models.CharField('Bairro', max_length=30)
    logradouro = models.CharField('Logradouro', max_length=40)
    numero = models.CharField('Número', max_length=10)
    telefone = models.CharField('Telefone', max_length=14)
    email = models.EmailField('E-mail', max_length=60, blank=True)
    latitude = models.CharField('Latitude', max_length=25)
    longitude = models.CharField('Longitude', max_length=25)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.razao_social
