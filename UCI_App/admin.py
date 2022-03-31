from django.contrib import admin
from .models import LoginLogoutLog
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta, Mapeo, RPropuestas, UsuariosConectados, NumHits, Conexiones


# Register your models here.

class LoginLogoutLogAdmin(admin.ModelAdmin):

    list_display = ('user','session_key','host','login_time','logout_time')


admin.site.register(LoginLogoutLog, LoginLogoutLogAdmin)

class CuentasAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")
    list_display = ('user','centro','hospital')

class MapasAdmin(admin.ModelAdmin):

    list_display = ('Centros','Servicio','Habitacion','VT','PEEP','RR','PPlato','PPeak','NumID')


class PropuestasAdmin(admin.ModelAdmin):
    list_display = ('user', 'mapa', 'value', 'MapID', 'created')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class NumHitsAdmin(admin.ModelAdmin):

    list_display = ('user','num')

class ConexionesAdmin(admin.ModelAdmin):

    list_display = ('nombre','conexion')

admin.site.register(UsuariosConectados)

admin.site.register(Cuenta, CuentasAdmin)

admin.site.register(Mapeo, MapasAdmin)

admin.site.register(RPropuestas, PropuestasAdmin)

admin.site.register(NumHits, NumHitsAdmin)

admin.site.register(Conexiones, ConexionesAdmin)







