-- Insertando datos en la tabla estado_pedido
INSERT INTO estado_pedido (estado_pedido) VALUES ('Pendiente');
INSERT INTO estado_pedido (estado_pedido) VALUES ('En Proceso');
INSERT INTO estado_pedido (estado_pedido) VALUES ('Completado');

-- Insertando datos en la tabla tipo_promocion
INSERT INTO tipo_promocion (tipo_promocion) VALUES ('Promoción de Lanzamiento');
INSERT INTO tipo_promocion (tipo_promocion) VALUES ('Oferta Especial');

-- Insertando datos en la tabla especialidad
INSERT INTO especialidad (nombre_especialidad) VALUES ('Herramientas');
INSERT INTO especialidad (nombre_especialidad) VALUES ('Materiales Básicos');
INSERT INTO especialidad (nombre_especialidad) VALUES ('Equipos de Seguridad');

-- Insertando datos en la tabla usuario (para clientes y vendedores)
INSERT INTO usuario (contrasenia, rol) VALUES ('password123', 'cliente');
INSERT INTO usuario (contrasenia, rol) VALUES ('securepassword456', 'vendedor');

-- Insertando datos en la tabla cliente
INSERT INTO cliente (id_usuario, nombre_cliente, email) VALUES (1, 'Juan Pérez', 'juan.perez@example.com');
INSERT INTO cliente (id_usuario, nombre_cliente, email) VALUES (2, 'Ana Gómez', 'ana.gomez@example.com');

-- Insertando datos en la tabla vendedor
INSERT INTO vendedor (id_especialidad, id_usuario, nombre_vendedor, email) VALUES (1, 2, 'Carlos López', 'carlos.lopez@example.com');

-- Insertando datos en la tabla sucursal
INSERT INTO sucursal (direccion, telefono) VALUES ('Calle Principal 123', '123-456-7890');
INSERT INTO sucursal (direccion, telefono) VALUES ('Avenida Central 456', '987-654-3210');

-- Insertando datos en la tabla categoria_producto
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (1, 'Herramientas Manuales');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (1, 'Herramientas Eléctricas');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (1, 'Materiales de Construcción');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Cemento');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Arena');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Ladrillos');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Acabados');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Pinturas');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Barnices');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (2, 'Cerámicos');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (3, 'Casos');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (3, 'Guantes');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (3, 'Lentes de Seguridad');
INSERT INTO categoria_producto (id_especialidad, nombre) VALUES (3, 'Accesorios Varios');

-- Insertando datos en la tabla producto
INSERT INTO producto (id_especialidad, id_categoria, codigo_upc, nombre, marca) VALUES (1, 1, 123456789012, 'Martillo de Uña', 'Stanley');
INSERT INTO producto (id_especialidad, id_categoria, codigo_upc, nombre, marca) VALUES (1, 2, 234567890123, 'Destornillador Philips', 'Bosch');
INSERT INTO producto (id_especialidad, id_categoria, codigo_upc, nombre, marca) VALUES (1, 5, 345678901234, 'Taladro Percutor', 'Bosch');
INSERT INTO producto (id_especialidad, id_categoria, codigo_upc, nombre, marca) VALUES (2, 9, 456789012345, 'Cemento Portland', 'Cemex');

-- Insertando datos en la tabla inventario
INSERT INTO inventario (id_sucursal, id_producto, cantidad) VALUES (1, 1, 100);
INSERT INTO inventario (id_sucursal, id_producto, cantidad) VALUES (1, 2, 150);
INSERT INTO inventario (id_sucursal, id_producto, cantidad) VALUES (2, 3, 50);
INSERT INTO inventario (id_sucursal, id_producto, cantidad) VALUES (2, 4, 200);

-- Insertando datos en la tabla mensaje
INSERT INTO mensaje (id_cliente, id_vendedor, titulo, mensaje, fecha_hora_envio) VALUES (1, 1, 'Consulta sobre producto', '¿Tienen disponible el taladro percutor en sucursal?', CURRENT_TIMESTAMP);

-- Insertando datos en la tabla pedido
INSERT INTO pedido (id_cliente, id_estado_pedido, fecha_pedido, moneda, conversion) VALUES (1, 1, CURRENT_DATE, 100000.0, 1.0);
INSERT INTO pedido (id_cliente, id_estado_pedido, fecha_pedido, moneda, conversion) VALUES (2, 2, CURRENT_DATE, 200000.0, 1.0);

-- Insertando datos en la tabla detalle_pedido
INSERT INTO detalle_pedido (id_pedido, id_producto, precio_unitario, cantidad) VALUES (1, 1, 25000.0, 2);
INSERT INTO detalle_pedido (id_pedido, id_producto, precio_unitario, cantidad) VALUES (2, 2, 15000.0, 1);

-- Insertando datos en la tabla promocion
INSERT INTO promocion (id_producto, id_tipo_promocion, fecha_inicio, fecha_termino) VALUES (1, 1, '2024-05-01', '2024-05-31');
INSERT INTO promocion (id_producto, id_tipo_promocion, fecha_inicio, fecha_termino) VALUES (2, 2, '2024-05-01', '2024-05-31');
