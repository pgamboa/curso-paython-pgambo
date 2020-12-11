class Admin():
    # Creo mi constructor
    def __init__(self, iden, nom):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.identificador = iden
        self.nombre = nom

    # Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return '[{}] ({})'.format(self.identificador, self.nombre)

    # Creo los metodos=acciones de mi clase
    # Se puede utilizar para realizar polimorfismo entre las Clases Admin-Cliente-Invitado
    def verProductos(self):
        """
        Ver productos
        """
        print("Ver el productos")

    def agregarProducto(self):
        """
        Agregar producto
        """
        print("Agregar producto")

    def eliminarProducto(self):
        """
        Eliminar producto
        """
        print("Eliminar producto")

    def modificarProducto(self):
        """
        Modificar producto
        """
        print("Modificar producto")

    def realizarEnvio(self):
        """
        Realizar Envío
        """
        print("Agregar producto")

    def confirmarEntrega(self):
        """
        Confirmar Entrega
        """
        print("Confirmar Entrega")


class Productos(Admin):
    # Creo mi constructor
    def __init__(self, grp, sgrp):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.grupo = grp
        self.sub_grupo = sgrp

    def __str__(self):
        return '[{}] ({})'.format(self.grupo, self.sub_grupo)


class Invitado():

    # Metodos para los Invitados
    # Creo los metodos=acciones de mi clase
    # Se puede utilizar para realizar polimorfismo entre las Clases Admin-Cliente-Invitado
    def verProductos(self):
        """
        Ver producto del invitado
        """
        print("Ver el producto de la clase Invitado")

    def registrarse(self):
        """
        Registrar el Invitado
        """
        print("Registrarse ")


class Clientesss(Admin):
    """
    docstring
    """

    def __init__(self, direc, phone):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.direccion = direc
        self.telefono = phone

    # Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return "Direccion: {} Telefono: {} ".format(self.direccion, self.telefono)

    # Metodos de la clase Clientes
    def comprarProducto(self):
        print("Comprar producto")

    def relaizarPago(self):
        print("Realizar pago")

    def anadirALaCesta(self):
        print("Añadir a la cesta")

    def borrarDeLaCesta(self):
        print("Borrar de la Cesta")


class Carro():
    # Creo mi constructor
    def __init__(self, n_producto, pro_1, pro_2, produccion, precio, total):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.nombre_producto = n_producto
        self.producto_1 = pro_1
        self.producto_2 = pro_2
        self.produccion = produccion
        self.total = total

    # Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return "Nombre del Producto: {} Producto_1: {} Producto_2: {} Producción: {} Total: {} ".format(self.nombre_producto, self.producto_1, self.producto_2, self.produccion, self.total)


class Pago():
    def __init__(self, i_cliente, n_cliente, t_tarjeta, n_tarjeta):
        self.identificador_clinete = i_cliente
        self.numero_clientes = n_cliente
        self.tipo_de_tarjeta = t_tarjeta
        self.numero_tarjeta = n_tarjeta

# Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return "Identificador_cliente: {} Numero_Cliente: {} Tipo de Tarjeta: {} Numero de Tarjeta: {} ".format(self.identificador_clinete, self.numero_clientes, self.tipo_de_tarjeta, self.numero_tarjeta)
