class cliente:
    def __init__(self, nombre, apellido, correo, telefono, comentarios):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.comentarios = comentarios

    def guardar_cliente(self):
        return "Cliente {} {} a sido gardado".format(self.nombre, self.apellido)

    def __repr__(self):
        return "cliente('{}','{}')".format(self.nombre, self.apellido)