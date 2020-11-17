from django.contrib import admin
from .models import Curso,Pagamento,Setor,Usuario,Atividade

class ListaCurso(admin.ModelAdmin):
    list_display = ('id','nome')

class ListaUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome')

class ListaSetor(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla')

class ListaPagamento(admin.ModelAdmin):
    list_display = ('id', 'pagamento')

class ListaAtividade(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Atividade, ListaAtividade)
admin.site.register(Curso, ListaCurso)
admin.site.register(Usuario, ListaUsuario)
admin.site.register(Setor, ListaSetor)
admin.site.register(Pagamento,ListaPagamento)