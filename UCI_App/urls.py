from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from UCI_App import views
from UCI_App.views import MapaDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'),name='login'),
    path('registrarse/', views.Log, name="Log"),
    path('inicio/', views.Inicio, name="Inicio"),
    path('mapa/', views.Mapa, name="Mapa"),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('<slug>', MapaDetailView.as_view(), name='detailmapa'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)