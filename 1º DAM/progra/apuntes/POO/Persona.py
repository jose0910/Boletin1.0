"""Crear una clase persona en la que tengo como propiedades su nombre, edad, dni, direccion y su nacionalidad
y luego crear 3 funciones: primera que me aparezca toda la informacion de la clase persona, segunda que me compruebe si la edad introducidad es correcta,
tercera: comprobar el dni"""

class Persona:
    def __init__(self, nombre, edad, dni, direccion, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.direccion = direccion
        self.nacionalidad = nacionalidad

    def mostrar_informacion(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad}\n"
            f"DNI: {self.dni}\n"
            f"Dirección: {self.direccion}\n"
            f"Nacionalidad: {self.nacionalidad}"
        )

    def comprobar_edad(self):
        if isinstance(self.edad, int) and 0 <= self.edad <= 120:
            return "Edad válida"
        else:
            return "Edad no válida"

    def comprobar_dni(self):
        # Suponiendo formato español: 8 dígitos + letra (ej. 12345678Z)
        import re
        patron_dni = r'^\d{8}[A-Z]$'
        if re.match(patron_dni, self.dni):
            return "DNI válido"
        else:
            return "DNI no válido"

