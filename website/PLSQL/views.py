from django.shortcuts import render
from django.db import connection
from .models import Seguradora, Automovel, Fatura
from datetime import datetime 

def home(request):
 return render(request, 'home.html')

def criarAutomovel(request):
 return render(request, 'criarAutomovel.html')

def criarSeguradora(request):
 return render(request, 'criarSeguradora.html')

def criarFatura(request):
 return render(request, 'criarFatura.html')

def mostrarDados(request):
 return render(request, 'mostrarDados.html')

#Função para criar uma seguradora

def criarSeguradoraBD(request):
    if request.method == 'POST':
        nif_seguradora = int(request.POST.get('nif_seguradora', 0))
        nome = request.POST.get('nome')
        morada = request.POST.get('morada')
        contacto = request.POST.get('contacto')
        website = request.POST.get('website')
        email = request.POST.get('email')

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CALL criar_seguradora(%s, %s, %s, %s, %s, %s);
                """,
                [nif_seguradora, nome, morada, contacto, website, email]
            )

        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html', {'success': False, 'error': 'Método inválido.'})

#Função para criar uma fatura

def criarFaturaBD(request):
    if request.method == 'POST':
        id_venda = int(request.POST.get('id_venda', 0))
        data_fatura_str = request.POST.get('data_fatura')
        forma_pagamento = request.POST.get('forma_pagamento')

        if data_fatura_str:
            data_fatura = datetime.fromisoformat(data_fatura_str)
        else:
            data_fatura = None

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CALL criar_fatura(%s, %s, %s);
                """,
                [id_venda, data_fatura, forma_pagamento]
            )

        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html', {'success': False, 'error': 'Método inválido.'})

#Função para criar um automóvel

def criarAutomovelBD(request):
    if request.method == 'POST':
        vin = int(request.POST.get('vin', 0))
        id_seguradora = int(request.POST.get('id_seguradora', 0)) or None
        nif_seguradora = int(request.POST.get('nif_seguradora', 0)) or None
        id_utilizador = int(request.POST.get('id_utilizador', 0))
        nif = int(request.POST.get('nif', 0))
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = int(request.POST.get('ano', 0))
        quilometragem = int(request.POST.get('quilometragem', 0)) or None
        preco = float(request.POST.get('preco', 0)) or None
        estado = request.POST.get('estado')
        cor = request.POST.get('cor')
        extras = request.POST.get('extras')
        imagem = request.POST.get('imagem')

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CALL criar_automovel(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """,
                [vin, id_seguradora, nif_seguradora,id_utilizador, nif, marca, modelo, ano, quilometragem, preco, estado, cor, extras, imagem]    
            )

        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html', {'success': False, 'error': 'Método inválido.'})


def mostrarDadosBD(request):
    automovel = Automovel.objects.all()
    seguradora = Seguradora.objects.all()
    fatura = Fatura.objects.all()

    return render(request, 'mostrarDados.html', {
        'automoveis': automovel,
        'seguradoras': seguradora,
        'faturas': fatura
    })



