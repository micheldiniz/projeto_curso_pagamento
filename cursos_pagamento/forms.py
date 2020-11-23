from django import forms
from datetime import datetime
from cursos_pagamento.models import Setor, Curso, Atividade, Usuario


class SetorForms(forms.ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {'setor_id': forms.HiddenInput()}

class ServidorForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'        
        exclude = ['user']

class CursoForms(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome','responsavel', 'carga_horaria','data_inicio', 'data_termino']
    
