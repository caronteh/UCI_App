from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PropuestasForm, MapasHitsForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Mapeo, RPropuestas, Cuenta, LoginLogoutLog, NumHits
from django.urls import reverse_lazy, reverse
from hitcount.views import HitCountDetailView
from django.db.models import Count
# Create your views here.

def Inicio(request):

    user='hades'
    estats = 0
    temp = 0
    id = 0
    count = User.objects.filter(last_login__startswith=timezone.now().date()).count()
    usuario = request.user
    cuentas = Cuenta.objects.all()
    logins = LoginLogoutLog.objects.all()
    form = MapasHitsForm(request.POST or None)
    propuestas = RPropuestas.objects.all()
    labels = []
    data = []

    queryset = NumHits.objects.order_by('-num')[:5]

    for user in queryset:

        labels.append(user.user)
        data.append(user.num)

    if request.method == 'POST':

        if form.is_valid():
            temp = request.POST.get("Opciones")
            user = User.objects.get(username=temp)
            id = user.id

        estats = RPropuestas.objects.filter(user=id).count()
        numero = NumHits.objects.get(user=user)
        numero.num = estats
        numero.save()



    return render(request,"inicio.html",{'cuentas':cuentas, 'usuario':usuario, 'count':count, 'propuestas': propuestas, 'logins':logins, 'form':form, 'estats':estats, 'labels':labels, 'data':data} )


def Log(request):

    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')


            return redirect('login')

    else:

        form= UserRegisterForm()

    context={'form': form }


    return render(request, "log.html", context)

def Mapa(request):


    count = User.objects.filter(last_login__startswith=timezone.now().date()).count()
    cuentas = Cuenta.objects.all()
    mapas = Mapeo.objects.all()
    user = request.user
    centro = Cuenta.objects.get(user=user)
    propuestas = RPropuestas.objects.filter(MapID=0)
    form = PropuestasForm(request.POST or None)



    if request.method == 'POST':

        mapa_id = request.POST.get('mapa_id')
        mapa_obj = Mapeo.objects.get(id=mapa_id)
        mapa_obj.Propuestas.add(user)




        if form.is_valid():
            temp = form.cleaned_data.get("Propuestas")

        opciones = RPropuestas(user=user, mapa_id=mapa_id, value=temp, MapID=mapa_id)
        propuestas = RPropuestas.objects.filter(MapID=mapa_id)

        opciones.save()


    return render(request, "mapa.html", {'mapas':mapas, 'user':user, 'form': form, 'cuentas':cuentas, 'count':count, 'propuestas': propuestas, 'centro':centro})


class MapaDetailView (HitCountDetailView):

   model = Mapeo
   template_name= "detailmapa.html"
   slug_field= "slug"
   count_hit = True

