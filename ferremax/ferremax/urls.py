from django.contrib import admin
from django.urls import path, include
from ferremax_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ferremax_app.urls')),
    path('', views.home, name='home'),
    path('iniciar_pago/', views.iniciar_pago, name='iniciar_pago'),
    path('exito_pago/', views.exito_pago, name='exito_pago'),
    path('registrar/',views.registrar, name ='registrar'),
    path('tasks/',views.tasks, name ='tasks'),
    path('logout/',views.cerrar_sesion, name ='logout'),
    path('ingresar/',views.ingresar, name ='ingresar'),
    path('ingresarproductos/',views.ingresar_productos, name ='ingresarproductos'),
    path('modificarproducto/', views.modificar_producto, name='modificar_producto'),
    path('eliminarproducto/', views.eliminar_producto, name='eliminar_producto'),
    path('listaproductos/', views.lista_productos, name='lista_productos'),
]
