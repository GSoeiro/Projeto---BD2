from django.db import models

class TipoUtilizador(models.Model):
    id_tipo_utilizador = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=80)

    class Meta:
        db_table = 'tipo_utilizador'
        managed = False


class Utilizador(models.Model):
    id_utilizador = models.AutoField(primary_key=True)
    nif = models.BigIntegerField(unique=True)
    id_tipo_utilizador = models.ForeignKey(
        TipoUtilizador, on_delete=models.PROTECT, db_column='id_tipo_utilizador'
    )
    nome = models.CharField(max_length=200)
    morada = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=200, unique=True)
    palavrapasse = models.CharField(max_length=200)
    data_criacao = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Ativo')

    class Meta:
        db_table = 'utilizador'
        managed = False

class Seguradora(models.Model):
    id_seguradora = models.AutoField(primary_key=True)
    nif_seguradora = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    morada = models.CharField(max_length=255, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'seguradora'
        managed = False


class Automovel(models.Model):
    id_automovel = models.AutoField(primary_key=True)
    vin = models.BigIntegerField(unique=True)
    id_utilizador = models.ForeignKey(Utilizador, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_utilizador')
    id_seguradora = models.ForeignKey(Seguradora, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_seguradora')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    quilometragem = models.BigIntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=30, choices=[('Novo', 'Novo'), ('Usado', 'Usado')], default='Usado')
    cor = models.CharField(max_length=50, null=True, blank=True)
    extras = models.TextField(null=True, blank=True)
    imagem = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'automovel'
        managed = False


class Colaborador(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    idade = models.IntegerField()

    class Meta:
        db_table = 'colaborador'
        managed = False


class Manutencao(models.Model):
    id_manutencao = models.AutoField(primary_key=True)
    id_automovel = models.ForeignKey(
        Automovel, on_delete=models.CASCADE, db_column='id_automovel'
    )
    id_colaborador = models.ForeignKey(
        Colaborador, on_delete=models.PROTECT, db_column='id_colaborador'
    )
    descricao = models.TextField()
    data_manutencao = models.DateField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'manutencao'
        managed = False

class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    id_automovel = models.ForeignKey(
        'Automovel',
        on_delete=models.PROTECT,
        db_column='id_automovel'
    )
    vin = models.BigIntegerField()  
    id_utilizador = models.ForeignKey(
        'Utilizador',
        on_delete=models.PROTECT,
        db_column='id_utilizador'
    )
    nif = models.BigIntegerField()  
    data_venda = models.DateField(null=True, blank=True)
    valor_venda = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    estado_venda = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'venda'
        managed = False


class Fatura(models.Model):
    id_fatura = models.AutoField(primary_key=True)
    id_venda = models.ForeignKey('Venda', on_delete=models.PROTECT, db_column='id_venda')
    data_fatura = models.DateTimeField(null=True, blank=True)
    forma_pagamento = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'fatura'
        managed = False

