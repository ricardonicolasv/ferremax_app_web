from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tipo_promocion', TipoPromocionViewSet)
router.register(r'especialidad', EspecialidadViewSet)
router.register(r'categoria_producto', CategoriaProductoViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'vendedor', VendedorViewSet)
router.register(r'sucursal', SucursalViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'estado_pedido', EstadoPedidoViewSet)
router.register(r'pedido', PedidoViewSet)
router.register(r'detalle_pedido', DetallePedidoViewSet)
router.register(r'promocion', PromocionViewSet)
router.register(r'mensaje', MensajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pago/iniciar/', iniciar_pago, name='iniciar_pago'),
    path('pago/exito/', exito_pago, name='exito_pago'),
]
