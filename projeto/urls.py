"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from website.views import home, criarAutomovelBD, criarAutomovel, criarSeguradora, criarSeguradoraBD, criarFatura, criarFaturaBD, mostrarDados, mostrarDadosBD, criarTipoUtilizador, criarTipoUtilizadorBD, criarUtilizador, criarUtilizadorBD

urlpatterns = [
 path('', home),
 path('criarAutomovel', criarAutomovel),
 path('criarAutomovelBD', criarAutomovelBD, name='criarAutomovelBD'),
 path('criarSeguradora', criarSeguradora),
 path('criarSeguradoraBD', criarSeguradoraBD, name='criarSeguradoraBD'),
 path('criarFatura', criarFatura),
 path('criarFaturaBD', criarFaturaBD, name='criarFaturaBD'),
 path('mostrarDados', mostrarDados),
 path('mostrarDadosBD', mostrarDadosBD, name='mostrarDadosBD'),
 path('criarTipoUtilizador', criarTipoUtilizador),
 path('criarTipoUtilizadorBD', criarTipoUtilizadorBD, name='criarTipoUtilizadorBD'),
 path('criarUtilizador', criarUtilizador),
 path('criarUtilizadorBD', criarUtilizadorBD, name='criarUtilizadorBD'),


]