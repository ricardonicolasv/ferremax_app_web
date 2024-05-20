from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes, IntegrationApiKeys
from django.http import HttpResponseRedirect
from .forms import RegistroForm, ProductoForm, EliminarProForm,ModificarForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ViewSets for your models
def home(request):
    return render(request, 'home.html')

class TipoPromocionViewSet(viewsets.ModelViewSet):
    queryset = TipoPromocion.objects.all()
    serializer_class = TipoPromocionSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer

# Configuración de las opciones de Transbank para integración
options = WebpayOptions(
    commerce_code=IntegrationCommerceCodes.WEBPAY_PLUS,  # Código de comercio de integración
    api_key=IntegrationApiKeys.WEBPAY,                  # API Key de integración
    integration_type="TEST"                             # Tipo de integración (cambiar a "LIVE" en producción)
)

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def iniciar_pago(request):
    try:
        # Obtener el detalle de pedido de la base de datos
        detalle_pedido = DetallePedido.objects.first()  # Obtener el primer detalle de pedido (ajustar según tu lógica)

        if not detalle_pedido:
            return render(request, 'error.html', {"message": "No hay detalles de pedido disponibles"})

        # Obtener los datos necesarios del detalle de pedido
        buy_order = str(detalle_pedido.id_pedido.id_pedido)  # Usar id_pedido como número de orden del pedido asociado al detalle
        session_id = str(detalle_pedido.id_pedido.id_pedido)  # Usar id_pedido como ID de sesión del pedido asociado al detalle
        amount = detalle_pedido.precio_unitario * detalle_pedido.cantidad  # Calcular el monto del detalle

        # Construir la URL de retorno
        return_url = request.build_absolute_uri(reverse('exito_pago'))

        # Crear la transacción utilizando los datos del detalle de pedido
        response = Transaction(options).create(buy_order, session_id, amount, return_url)

        logger.info("Response from Transbank: %s", response)

        # Verificar si la respuesta contiene un token y una URL para redirigir al usuario
        if response.get('token') and response.get('url'):
            # Redireccionar al usuario a la URL de inicio de pago proporcionada por Transbank
            logger.info("Redirecting user to Transbank payment page.")
            return HttpResponseRedirect(response['url'])
        else:
            # Manejar cualquier error que ocurra durante la creación de la transacción
            logger.error("Error starting payment: %s", response)
            return render(request, 'error.html', {"message": "Error al iniciar el pago", "details": response})
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante el procesamiento
        logger.exception("Error processing request: %s", str(e))
        return render(request, 'error.html', {"message": "Error al procesar la solicitud", "error": str(e)})
@csrf_exempt
@api_view(['GET'])
def exito_pago(request):
    try:
        token = request.GET.get('token_ws')
        response = Transaction(options).commit(token)

        if response.get('status') == 'AUTHORIZED':
            # Devolver una respuesta JSON utilizando JsonResponse
            return JsonResponse({"message": "Pago exitoso", "details": response}, status=200)
        else:
            # Devolver una respuesta JSON utilizando JsonResponse
            return JsonResponse({"message": "Error en el pago", "details": response}, status=500)
    except Exception as e:
        # Devolver una respuesta JSON utilizando JsonResponse
        return JsonResponse({"message": "Error al procesar la solicitud", "error": str(e)}, status=500)
    

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_completo = form.cleaned_data.get('nombre_completo')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            # Verifica que las contraseñas ingresadas sean iguales
            if password != confirmar_password:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'Las contraseñas no coinciden.'
                })

            try:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre_completo)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'El correo electrónico ya está registrado.'
                })
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def tasks(request):
    return render (request, 'tasks.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Maneja el caso en que el usuario no esté registrado, la contraseña sea incorrecta
                # o el correo electrónico esté mal formateado
                return render(request, 'ingresar.html', {
                    'form': form,
                    'error': 'Correo electrónico o contraseña incorrectos.'
                })
        else:
            # Maneja el caso en que el correo electrónico esté mal formateado
            return render(request, 'ingresar.html', {
                'form': form,
                'error': 'Por favor ingrese un correo electrónico válido.'
            })
    else:
        form = AuthenticationForm()
    return render(request, 'ingresar.html', {'form': form})

def ingresar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresarproductos')
    else:
        form = ProductoForm()
    return render(request, 'ingresarproductos.html', {'form': form})

def modificar_producto(request):
    if request.method == 'POST':
        form = ModificarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ModificarForm()
    return render(request, 'modificarproducto.html', {'form': form})


def eliminar_producto(request):
    if request.method == 'POST':
        form = EliminarProForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['nombre_producto']
            producto.delete()
            return redirect('lista_productos')  # Redireccionar después de eliminar el producto
    else:
        form = EliminarProForm()
    return render(request, 'eliminarproducto.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listaproductos.html', {'productos': productos})
    