"""projeto_curso_pagamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfr
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cursos_pagamento.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login_pagina', login_pagina, name='login_pagina'),
    path('logout_pagina', logout_pagina, name='logout_pagina'),
    path('login', login, name='login'),
    path('cadastra_setor', cadastro_setor, name='cadastra_setor'),
    path('cadastra_servidor', cadastro_servidor, name='cadastra_servidor'),
    path('cadastra_curso', cadastro_curso, name='cadastra_curso'),
    path('deleta_setor/<int:setor_id>', deleta_setor, name='deleta_setor'),
    path('setores', visualiza_setores, name='visualiza_setores'),   
    path('edita_setor/<int:setor_id>', edita_setores, name='edita_setores'),  
    path('dashboard', dashboard, name='dashboard'),
    path('pagina_setor', pagina_setor, name='pagina_setor'),
    path('pagina_servidor', pagina_servidor, name='pagina_servidor'),
    path('pagina_curso', pagina_curso, name='pagina_curso'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
