"""receiving_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from login.views import *
from cenditel.views import ListarEvento, ListarUsuario, Index, ListarRevista, ListarCurso, ListarInvestigador, ListarProyecto, ListarLibro, ListarParticipante
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', auth_views.PasswordResetDoneView.as_view()),
    #path(r'index/', index),
    #path(r'^register/$', register),
    #path(r'^register/success/', register_success),
    path(r'accounts/login/', auth_views.LoginView.as_view),
    #path(r'^logout/', logout_page),
    path(r'index/', Index.as_view(), name='index'),
    #path(r'^listar-eventos/', ListarEvento.as_view(), name='eventos'),
    #path(r'^listar-usuarios/', ListarUsuario.as_view(), name='usuarios'),
    #path(r'^listar-revistas/', ListarRevista.as_view(), name='revistas'),
    #path(r'^listar-cursos/', ListarCurso.as_view(), name='cursos'),
    #path(r'^listar-investigadores/', ListarInvestigador.as_view(), name='investigadores'),
    #path(r'^listar-proyectos/', ListarProyecto.as_view(), name='proyectos'),
    #path(r'^listar-libros/', ListarLibro.as_view(), name='libros'),
    #path(r'^listar-participantes/', ListarParticipante.as_view(), name='participantes'),
]
