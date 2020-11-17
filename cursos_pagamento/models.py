from django.db import models
from django.contrib.auth.models import User

class Setor(models.Model):
    class Meta:
        verbose_name = 'setor'
        verbose_name_plural = 'Setores'

    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=10)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    login = models.CharField(max_length=15)
    is_chefe = models.BooleanField(default=False, verbose_name='Chefe de setor?')

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NOVO = 'NOVO'
    INICIADO = 'INICIADO'
    FINALIZADO = 'FINALIZADO'

    SITUACAO_CURSO = [
        (NOVO,'novo'),
        (INICIADO,'iniciado'),
        (FINALIZADO,'finalizado')
    ]
    nome = models.CharField(max_length=200)
    responsavel = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name='usuario_responsavel')
    carga_horaria = models.CharField(max_length=15, null=True)
    data_inicio = models.DateField(null=True)
    data_termino = models.DateField(null=True)
    participante = models.ManyToManyField(Usuario, through='Atividade')
    has_started = models.BooleanField(default=False, verbose_name='curso iniciado')
    has_finished = models.BooleanField(default=False, verbose_name='curso finalizado')
    situacao_curso = models.CharField(max_length=20,choices=SITUACAO_CURSO,default=NOVO,)
    valor_total_curso = models.CharField(editable=False, max_length=100, null=True, verbose_name='Valor total pago pelo curso')
    

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    horas_trabalhadas = models.CharField(max_length=15)
    relatorio = models.FileField(upload_to='relatorio/%d/%m/%Y/')
    complementacao = models.CharField(max_length=100, null=True, verbose_name='Complementação')
    validation_date = models.DateField(editable=False, null=True)
    is_validated = models.BooleanField(default=False)
    valor_pago_servidor = models.CharField(editable=False, max_length=100, null=True, verbose_name='Valor pago para o servidor')

    # def __str__(self):
    #     return self.curso.nome


class Pagamento(models.Model):
    user = models.ManyToManyField(User)
    curso = models.ManyToManyField(Curso)
    pagamento = models.CharField(max_length = 10)

    def __str__(self):
        return f'curso: {self.user}, instrutor: {self.curso}, pagamento: {self.pagamento}'