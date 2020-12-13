class Admin():  # Es mi super clase
    # Constructor de Admin
    def __init__(self, identificador, nombre):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.identificador = identificador
        self.nombre = nombre
        self.veProductos = False
        self.agregaProducto = False
        self.eliminaProducto = False
        self.modificaProducto = False
        self.realizaEnvio = False
        self.confirmaEntrega = False

    # Redefine el método que se va ha ejecutar, debe retornar un STR

    def __str__(self):
        return f"El Identificador es: {self.identificador}, y le corresponde el Nombre: {self.nombre}"

    # Creo los metodos=acciones de mi clase Padre
    # Se puede utilizar para realizar polimorfismo entre las Clases Admin-Cliente-Invitado
    def verProductos(self, vproducto, stock=0):
        """
        Ver productos
        """
        self.revisado = vproducto
        if vproducto == True:
            self.veProductos = True
            print(f"El producto existe {self.veProductos}")
        else:
            self.veProductos = False
            print(f"No existe el producto, el Stock = {stock} ")

    def agregarProducto(self):
        """
        Agregar producto
        """
        self.agregaProducto = True
        print("Agregar producto")

    def eliminarProducto(self):
        """
        Eliminar producto
        """
        self.eliminaProducto = True
        print("Eliminar producto")

    def modificarProducto(self):
        """
        Modificar producto
        """
        self.modificaProducto = False
        print("Modificar producto")

    def realizarEnvio(self):
        """
        Realizar Envío
        """
        #self.autorizar_envio = enviado
        if self.veProductos == self.agregaProducto == True:
            self.realizaEnvio = True
            print(f"El producto será enviado")
        else:
            print("Realizar confirmación")
            self.realizaEnvio = False
        return self.realizaEnvio

    def confirmarEntrega(self, realizaEnvio):
        """
        Confirmar Entrega
        """
        #self.confirmado = realizaEnvio
        if realizaEnvio == True:
            print("EL producto fue enviado y recibido")
            self.confirmaEntrega = True
        else:
            print("El producto aún no se recibe por el cliente")
            self.confirmaEntrega = False

    def estado(self):
        print(f"El Administrador es: {self.nombre}\
            \nCon CI: {self.identificador}\
            \nEl producto fue revisado: {self.veProductos}\
            \nSe agrego los productos? {self.agregaProducto},\
            \nLos productos caducados fueron retirados {self.eliminaProducto}\
            \nSe actualizaron los productos? {self.modificaProducto}.\
            \nSe realiza el envío?: {self.realizaEnvio}\
            \nCliente confiram la recepción {self.confirmaEntrega} ")


class Productos(Admin):
    # Constructor Productos()
    def __init__(self, grupo, sub_grupo, identificador, nombre):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        # Con super() llamo al contructor de la Clase Padre con sus dos parámetros marca, mode
        super().__init__(identificador, nombre)
        self.grupo = grupo
        self.sub_grupo = sub_grupo

    def __str__(self):
        return '[{}] ({})'.format(self.grupo, self.sub_grupo)


class Invitado(Productos):
    # Metodos para los Invitados
    # Creo los metodos=acciones de mi clase
    # Se puede utilizar para realizar polimorfismo entre las Clases Admin-Cliente-Invitado
    def __init__(self, grupo, sub_grupo, identificador, nombre):
        # Con super() llamo al contructor de la Clase Padre con sus dos parámetros marca, modelo
        super().__init__(grupo, sub_grupo, identificador, nombre)

    def verProductos(self):
        productos = ['A', 'B', 'C', 'D', 'E']
        for p in productos:
            print(f"Los productos en Stock son: {p} ")
        """
        Ver producto del invitado
        """

    def registrarse(self, identificador, nombre):
        invitados = []
        contador = 0
        invitados.append(nombre)

        for i in invitados:
            contador += 1
            print(f"La lista los invitados registrados son: {i}\
                 \ny el número de invitados es {contador} ")

        """
        Registrar el Invitado
        """


class Cliente(Productos):
    """
    docstring
    """
    # Constructor de Clientes

    def __init__(self, direccion, telefono):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.direccion = direccion
        self.telefono = telefono

    # Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return f"Direccion: {self.direccion} Telefono: {self.telefono} "

    # Metodos de la clase Clientes
    def comprarProducto(self):
        print("Comprar producto")

    def relaizarPago(self, pago):
        if pago == True:
            print("Emitir factura")
        else:
            print("Llamar a los señores policias")

    def anadirALaCesta(self):
        print("Añadir a la cesta")

    def borrarDeLaCesta(self):
        print("Borrar de la Cesta")


class Pago(Cliente):
    def __init__(self, identificador_cliente, nombre_clientes, tipo_de_tarjeta, numero_tarjeta):
        self.identificador_cliente = identificador_cliente
        self.numero_clientes = nombre_clientes
        self.tipo_de_tarjeta = tipo_de_tarjeta
        self.numero_tarjeta = numero_tarjeta

    def __str__(self):
        return f"Identificador_cliente: {self.identificador_cliente} Numero_Cliente: {self.numero_clientes}\
             Tipo de Tarjeta: {self.tipo_de_tarjeta} Numero de Tarjeta: {self.numero_tarjeta} "
    



class Carro(Cliente):
    # Creo mi constructor
    def __init__(self, numero_producto, producto_1, producto_2, produccion, precio=0, total=0):
        # creo los atributos de isntancia con los argumentos que se llaman en las clases
        self.numero_producto = numero_producto
        self.producto_1 = producto_1
        self.producto_2 = producto_2
        self.produccion = produccion
        self.precio = precio
        self.total = total

    # Redefine el método que se va ha ejecutar, debe retornar un STR
    def __str__(self):
        return f"NumeroProducto: {self.numero_producto} Producto_1: {self.producto_1} Producto_2: {self.producto_2}\
             Producción: {self.produccion} Precio: {self.precio} Total: {self.total} "


if __name__ == "__main__":
    # Creo miinstancia admin de mi clase Admin()
    admin = Admin('1803082872', 'Pablo Gamboa')
    admin.verProductos(True)
    admin.agregarProducto()
    admin.realizarEnvio()
    envio = True
    admin.confirmarEntrega(envio)
    print(admin.estado())

    # Creo mi instancia producto de mi clase Producto(Admin)
    producto = Productos('Regalos', 'Tecnología', 123456789, 'Pepito ')
    producto.verProductos(True)
    producto.agregarProducto()
    producto.realizarEnvio()
    print(producto.estado())

    invitado = Invitado('Regalos', 'Ropa', '222333555', 'Invitado 1')
    invitado.verProductos()
    invitado.registrarse('4444555566', 'Juanpigue')

    cliente = Cliente('Oriente y 16 de octubre', '00124587')
    cliente.relaizarPago(False)
    cliente.verProductos(True)

    pago=Pago('789456','Pericos','Credito',789456325)
    pago.comprarProducto()

    carro=Carro('ADE56','A','B','2020')
