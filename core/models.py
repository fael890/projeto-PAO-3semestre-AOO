from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIAS_CHOICES = (
    ('padaria', 'Padaria'),
    ('hortifruti', 'Hortifruti'),
    ('acougue', 'Açougue'),
    ('bebidas', 'Bebidas'),
)

class Endereco(models.Model):
    cep = models.CharField(max_length=100, verbose_name='CEP')
    estado = models.CharField(max_length=2, verbose_name='Estado')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    rua = models.CharField(max_length=100, verbose_name='Rua')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    numero = models.IntegerField(blank=True, null=True, verbose_name='Número')

    class Meta:
        verbose_name_plural = 'Endereço'

    def __str__(self):
        return self.cep

class Mercado(models.Model):
    razao_social = models.CharField(max_length=100, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    endereco = models.OneToOneField(Endereco, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Endereço')

    class Meta:
        verbose_name_plural = 'Mercado'

    def __str__(self):
        return self.razao_social

class Promocao(models.Model):
    descricao = models.CharField(max_length=150, blank=True, null=True, verbose_name='Descricao')
    unidade = models.CharField(max_length=20, blank=True, null=True, verbose_name='Unidade')
    categoria = models.CharField(max_length=100,choices=CATEGORIAS_CHOICES, blank=True, null=True, verbose_name='Categoria')
    preco_normal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço normal')
    preco_promocao = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    data_inicio = models.DateField(auto_now=False, verbose_name='Inicio')
    data_fim = models.DateField(auto_now=False, verbose_name='Fim')
    distancia = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Distância')
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE, verbose_name='Mercado')
    imagem = models.ImageField(upload_to='img_promocoes', blank=True, null=True, verbose_name="ImagemPromoção")
    marca = models.CharField(max_length=100, blank=True, null=True, verbose_name='Marca')
    valor_energetico = models.CharField(max_length=100, blank=True, null=True, verbose_name='Valor Energético')
    ingredientes = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ingredientes')
    informacao_adicional = models.CharField(max_length=100, blank=True, null=True, verbose_name='Informação adicional')

    class Meta:
        verbose_name_plural = 'Promoções'

    def __str__(self):
        return self.descricao

class ListaCompras(models.Model):
    id_promocao = models.ForeignKey(Promocao, on_delete=models.CASCADE, verbose_name='Promoção')
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')

    class Meta:
        verbose_name_plural = 'lista compras'

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    imagem = models.ImageField(upload_to='img_usuario', blank=True, null=True, verbose_name='')
    id_lista_compras = models.ForeignKey(ListaCompras, blank=True, null=True, on_delete=models.CASCADE, verbose_name='ListaCompras')
    endereco = models.OneToOneField(Endereco, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Endereço')
    autenticacao = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Usuario'

    def __str__(self):
        return self.email



