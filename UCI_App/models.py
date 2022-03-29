from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from autoslug import AutoSlugField

class LoginLogoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)


    class Meta:
        db_table = 'Entradas y Salidas'
        verbose_name = 'Entrada o Salida'
        verbose_name_plural ='Entradas y Salidas'

    def __str__(self):
        return self.user.username

class Cuenta(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    centro = models.CharField(max_length=15,choices=[('JX','JX'),('VH','VH')])
    hospital = models.CharField(max_length=15, choices=[('JoanXXIII', 'JoanXXIII'), ('VallHebron', 'VallHebron')])
    imagen = models.ImageField(upload_to='media/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Cuenta'
        verbose_name_plural ='Cuentas'

    def __str__(self):
        return self.user.username


class Mapeo(models.Model):

    slug = AutoSlugField(populate_from='NumID', blank=True)
    Centros = models.CharField('Centro',max_length=15,choices=[('VH','VH'),('JX','JX')], blank=True)
    Servicio = models.CharField('Servicio',max_length=15,choices=[('UCI1','UCI1'),('UCI2','UCI2'),
    ('UCIA','UCIA'),('UCIP','UCIP'),('UCIN','UCIN')])
    Habitacion = models.CharField('Habitacion',max_length=15,choices=[('BOX01','BOX01'),('BOX02','BOX02')])
    NumID = models.IntegerField('NumID', null=True)
    MP = models.FloatField('MP',null=True)
    VT = models.FloatField('VT',null=True)
    PEEP = models.FloatField('PEEP',null=True)
    RR = models.FloatField('RR',null=True)
    PPlato = models.FloatField('PPlato',null=True)
    PPeak = models.FloatField('PPeak',null=True)
    Propuestas = models.ManyToManyField(User, default=None, blank=True,related_name='liked')

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'

    @property
    def num_likes(self):

        return self.liked.all().count()

    def __str__(self):
        return self.Centros

VALUE_CHOICES = ( ('Ninguna me convence', 'Ninguna me convence'), ('Bajar VT', 'Bajar VT'),
    ('Bajar PEEP','Bajer PEEP'),('Bajar RR','Bajar RR')

)

class RPropuestas (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mapa = models.ForeignKey(Mapeo, on_delete=models.CASCADE)
    value = models.CharField( default='No me convence', max_length=25)
    MapID = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=now, null=True)

    class Meta:
        verbose_name = 'Propuesta'
        verbose_name_plural = 'Propuestas'

class UsuariosConectados (models.Model):

    numero = models.IntegerField(blank=True)


class NumHits (models.Model):

    user = models.CharField(max_length=15)
    num = models.IntegerField(null=True)

    class Meta:

        verbose_name = 'Hit'
        verbose_name_plural = 'Hits'


