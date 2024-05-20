from django.db import models

class TipoPromocion(models.Model):
    tipo_promocion = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_promocion

    class Meta:
        db_table = 'tipo_promocion'


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_especialidad

    class Meta:
        db_table = 'especialidad'


class CategoriaProducto(models.Model):
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='id_especialidad')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_producto'


class Usuario(models.Model):
    contrasenia = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.rol

    class Meta:
        db_table = 'usuario'


class Cliente(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    nombre_cliente = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        db_table = 'cliente'


class Vendedor(models.Model):
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='id_especialidad')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    nombre_vendedor = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_vendedor

    class Meta:
        db_table = 'vendedor'


class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'sucursal'


class Producto(models.Model):
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, db_column='id_especialidad')
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, db_column='id_categoria')
    codigo_upc = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.marca} - {self.id_especialidad.nombre_especialidad}"

    class Meta:
        db_table = 'producto'


class Inventario(models.Model):
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, db_column='id_sucursal')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.id_producto.nombre} - {self.cantidad}"

    class Meta:
        unique_together = ('id_sucursal', 'id_producto')
        db_table = 'inventario'


class EstadoPedido(models.Model):
    estado_pedido = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_pedido

    class Meta:
        db_table = 'estado_pedido'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True, default=1)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, db_column='id_estado_pedido')
    fecha_pedido = models.DateField()
    moneda = models.FloatField()
    conversion = models.FloatField()

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.id_cliente.nombre_cliente} - {self.id_estado_pedido.estado_pedido}"

    class Meta:
        db_table = 'pedido'


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    precio_unitario = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.id_producto.nombre} - {self.cantidad} - {self.precio_unitario}"

    class Meta:
        db_table = 'detalle_pedido'


class Promocion(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, db_column='id_producto')
    id_tipo_promocion = models.ForeignKey(TipoPromocion, on_delete=models.CASCADE, db_column='id_tipo_promocion')
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()

    def __str__(self):
        return f"{self.id_producto.nombre} - {self.id_tipo_promocion.tipo_promocion}"

    class Meta:
        unique_together = ('id_producto', 'id_tipo_promocion')
        db_table = 'promocion'


class Mensaje(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, db_column='id_vendedor')
    titulo = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=255)
    fecha_hora_envio = models.DateTimeField()

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'mensaje'
