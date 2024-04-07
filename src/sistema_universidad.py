from enum import Enum
import random

class Universidad:
    # constructor
    def __init__(self) -> None:
        self.listado_alumnos = []
        self.listado_profesores = []
        self.listado_asignaturas = []

    # Añadir asignaturas que se imparten en la universidad
    def añadir_asignatura(self, nombre, codigo:int, creditos:int):
        print('Asignatura: ' + nombre +'\n' + 'Código: ' + str(codigo) + '\n' + 'Creditos: ' + str(creditos))
        
        # Para gestionar la entrada que se pide al usuario hago uso de un try/except
        # en caso de que algo falle durante la entrada se controlará gracias a eso.
        try:
            respuesta = int(input("Si los datos son correctos pulse 0, en caso contrario pulse 1: "))
            if respuesta == 0:
                asignatura = Asignatura(nombre, codigo, creditos)
                self.listado_asignaturas.append(asignatura)
                print('Asignatura añadida')
            else:
                print("Datos incorrectos")

        except ValueError:
            print("Error: Debes ingresar un número entero.")

    # Para gestionar la entrada de alumnos a la Universidad
    def matricular_alumno(self, curso:int, nombre, DNI:str, direccion:str, sexo:str):
        print('Curso: ' + str(curso) +'\n' + 'Nombre: ' + nombre + '\n' + 'DNI: ' + DNI + '\n' + 'Direccion: ' + direccion + '\n' + 'sexo: ' + sexo)
        
        # Nuevamente se hace uso del control de la excepción en caso de algun fallo en la solicitud al usuario:
        try:
            respuesta = int(input("Si los datos son correctos pulse 0, en caso contrario pulse 1: "))
            if respuesta == 0:
                alumno = Estudiante(curso, nombre, DNI, direccion, sexo)
                self.listado_alumnos.append(alumno)
            else:
                print("Los datos no son correctos.")

        except ValueError:
            print("Error: Debes ingresar un número entero.")
    
    # Método para el control del contrato de un profesor nuevoa  a la universidad
    def contratar_profesor(self, nombre, DNI, direccion:str, sexo:str, titular:bool):
        print('Nombre: ' + nombre + '\n' + 'DNI: ' + DNI + '\n' + 'Direccion: ' + direccion + '\n' + 'sexo: ' + sexo)
        
        # En este también se hace uso del control de la excepción pero teneiendo en cuenta de si el profesor es titular o asociado
        try:    
            respuesta = int(input("Si los datos son correctos pulse 0, en caso contrario pulse 1: "))
            if respuesta == 0:
                if titular is True:
                    area_investigacion = input("Por favor, introduce su area de investigacion: ")
                    profesor = ProfesorTitular(area_investigacion, nombre, DNI, direccion, sexo)
        
                else:
                    trabajo_externo = input("Por favor, introduce su trabajo externo (si no tiene dejar vacío): ")
                    if not trabajo_externo:  # Si el usuario no ingresó nada (cadena vacía)
                        trabajo_externo = None
                    profesor = ProfesorAsociado(trabajo_externo, nombre, DNI, direccion, sexo)
                self.listado_profesores.append(profesor)

            else: 
                print("Datos incorrectos")

        except ValueError:
            print("Error: Valor no reconocido.")

    # MEtodos para obtener el objeto según el dni ya que es un dpcumento único para cada persona:
    def obtener_profesor(self, DNI):
        for profesor in self.listado_profesores:
            if profesor.DNI == DNI:
                return profesor
        return None
    
    def obtener_alumno(self, DNI):
        for alumno in self.listado_alumnos:
            if alumno.DNI == DNI:
                return alumno
        return None

    # Metodos para gestionar la salida de los alumnos:
    def DarBaja_alumno(self, curso: int, nombre: str, DNI: str, direccion: str, sexo: str):
        # Se hace uso de las funciones obtener para facilitar la búsqueda:
        alumno = self.obtener_alumno(DNI) 
        if alumno is not None:
            self.listado_alumnos.remove(alumno)
            print(f"Se ha dado de baja al alumno con DNI: {DNI}")
        else:
            print(f"No se ha encontrado al estudiante con DNI: {DNI}")

    #Se sigue la misma idea qeu en el anterior metodo pero teniendo en cuenat los créditos que posee el alumno
    def graduar_alumno(self, curso:int, nombre:str, DNI:str, direccion:str, sexo:str):
        alumno = self.obtener_alumno(DNI)
        if alumno is not None:
            if alumno.creditos == 240:
                self.listado_alumnos.remove(alumno)
                print(f"Se ha graduado al alumno con DNI: {DNI}")
            else:
                print("Créditos insuficientes")
        else:
            print(f"No se ha encontrado al estudiante con DNI: {DNI}")

    # MEtodos para gestionar la salida de los profesores:
    def despedir_profesor(self, nombre:str, DNI:str, direccion:str, sexo:str, titular:bool):
        profesor = self.obtener_profesor(DNI)
        if profesor is not None:
            self.listado_profesores.remove(profesor)
            print(f"Se ha despedido al profesor con DNI: {DNI}")
        else:
            print(f"No se ha encontrado al profesor con DNI: {DNI}")

    def jubilar_profesor(self, nombre:str, DNI, direccion:str, sexo:str, titular:bool):
        profesor = self.obtener_profesor(DNI)
        if profesor is not None:
            self.listado_profesores.remove(profesor)
            print(f"Se ha jubilado al profesor con DNI: {DNI}")
        else:
            print(f"No se ha encontrado al profesor con DNI: {DNI}")
    
    # Métodos para actualizar los datos de las personas de la Universidad:
    def actualizar_datos_estudiante(self, DNI, nombre=None, direccion=None, sexo=None, curso=None, creditos=None, asignatura=None):
        estudiante = self.obtener_alumno(DNI)
        if estudiante is not None:
            if nombre is not None:
                estudiante.nombre = nombre
            if direccion is not None:
                estudiante.direccion = direccion
            if sexo is not None:
                estudiante.sexo = sexo
            if curso is not None:
                estudiante.curso = curso
            if creditos is not None:
                estudiante.creditos = creditos
            print(f"Se han actualizado los datos del estudiante con DNI: {DNI}")
        else:
            print(f"No se ha encontrado al estudiante con DNI: {DNI}")

    def actualizar_datos_profesor(self, DNI, nombre=None, direccion=None, sexo=None, area_investigacion=None, trabajo_externo=None):
        profesor = self.obtener_profesor(DNI)
        if profesor is not None:
            if nombre is not None:
                profesor.nombre = nombre
            if direccion is not None:
                profesor.direccion = direccion
            if sexo is not None:
                profesor.sexo = sexo
            if isinstance(profesor, ProfesorTitular) and area_investigacion is not None:
                profesor.area_investigacion = area_investigacion
            if isinstance(profesor, ProfesorAsociado) and trabajo_externo is not None:
                profesor.trabajo_externo = trabajo_externo
            print(f"Se han actualizado los datos del profesor con DNI: {DNI}")
        else:
            print(f"No se ha encontrado al profesor con DNI: {DNI}")


class Persona:
    def __init__(self, nombre:str, DNI:str, direccion:str, sexo:str) -> None:
        self.nombre = nombre
        if self.validar_identidad(DNI):
            self.DNI = DNI
        else:
            raise ValueError("Documento de Identidad no válido")
        self.direccion = direccion
        if sexo in ['M', 'H']:
            self.sexo = sexo
        else:
            raise ValueError("Género no válido")

    def __str__(self) -> str:
        return  'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion  
 
    # Metodo para la validadcion de DNI/NIE:
    def validar_identidad(self, dni:str):
        tabla_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        tabla_letras_nie = "TRWAGMYFPDXBNJZSQVHLCKE"
        documento = dni.upper() # Mayusculas
        #La idea se basa en la longitud y los digitos de numero y letra
        if len(documento) == 9 and documento[:8].isdigit() and documento[8] in tabla_letras:
            numero_documento = int(documento[:8])
            letra_documento = documento[8]
            letra_calculada = tabla_letras[numero_documento % 23]
            return letra_documento == letra_calculada
        #La misma idea para el caso del NIE
        elif len(documento) == 9 and documento[0] in "XYZ" and documento[1:8].isdigit() and documento[8] in tabla_letras_nie:
            if documento[0] == "X":
                numero_documento = int("0" + documento[1:8])
            elif documento[0] == "Y":
                numero_documento = int("1" + documento[1:8])
            elif documento[0] == "Z":
                numero_documento = int("2" + documento[1:8])
            letra_documento = documento[8]
            letra_calculada = tabla_letras_nie[numero_documento % 23]
            return letra_documento == letra_calculada
        else:
            return False


class Profesor(Persona):
    def __init__(self, nombre, DNI, direccion, sexo) -> None:
        # Herencia
        super().__init__(nombre, DNI, direccion, sexo)

        self.asignaturas = []
        self.creditos = None
        self.departamento = None

    def __str__(self) -> str:
        return 'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion 

    def asignar_asignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
        else:
            print("Asignatura ya añadida")

    def quitar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            print("La asignatura no está asignada a este profesor.")

    def asignar_departamento(self, departamento):
        if departamento in EDep: # Debe ser un departamento de las opciones del enunciado de la clase Enum
            self.departamento = departamento
        else:
            print("El departamento no es válido.")


class ProfesorTitular(Profesor):
    def __init__(self, area_investigacion, nombre, DNI, direccion, sexo) -> None:
        super().__init__(nombre, DNI, direccion, sexo)
        self.area_investigacion = area_investigacion
        asignaturas = []
    # Metodod para cambiar el area de investigacion:
    def cambiar_areaIVN(self, nuevo_area):
        self.area_investigacion = nuevo_area

    def __str__(self) -> str:
        asignaturas_str = ', '.join(str(asignatura) for asignatura in self.asignaturas)
        return f"Nombre: {self.nombre}\nDNI: {self.DNI}\nDirección: {self.direccion}\nGénero: {self.sexo}\nÁrea de Investigación: {self.area_investigacion}\nAsignaturas: {asignaturas_str}"

class ProfesorAsociado(Profesor):
    def __init__(self, trabajo_externo, nombre, DNI, direccion, sexo) -> None:
        super().__init__(nombre, DNI, direccion, sexo)
        self.trabajo_externo = trabajo_externo

    def __str__(self) -> str:
        asignaturas_str = ', '.join(str(asignatura) for asignatura in self.asignaturas)
        return f"Nombre: {self.nombre}\nDNI: {self.DNI}\nDirección: {self.direccion}\nGénero: {self.sexo}\nTrabajo externo: {self.trabajo_externo}\nAsignaturas: {asignaturas_str}"

class Estudiante(Persona):
    def __init__(self, curso, nombre, DNI, direccion, sexo) -> None:
        
        super().__init__(nombre, DNI, direccion, sexo)
        self.curso = curso
        self.creditos = 0
        self.num_expediente = int(''.join(random.choices('0123456789', k=6)))
        self.lista_asignaturas = []

    def __str__(self) -> str:
        return 'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'Nº Expediente: ' + str(self.num_expediente) + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion + '\n' + 'Curso de más creditos matriculado: ' + str(self.curso) + '\n' +  'Creditos: ' + str(self.creditos) +'\n' +  'Asignaturas matriculado: ' + str(self.lista_asignaturas)
    #Metodos para controlar las asignaturas del estduiante
    def matricular_asignaturas(self, asignatura):
        if asignatura not in self.lista_asignaturas:
            self.lista_asignaturas.append(asignatura)
        else:
            print('Asignatura ya añadida')

    def aprobar_asignatura(self, asignatura):
        if asignatura in self.lista_asignaturas:
            self.creditos += asignatura.creditos #La suma de creditos irá aumentando mediante va aprobando asignaturas el alumno
            self.lista_asignaturas.remove(asignatura)
        else:
            print("Asignatura no encontrada")
              

class EDep(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Departamento:
    def __init__(self, nombre_dep:EDep) -> None:
        self.nombre_dep = nombre_dep
        self.profesores = [] # Un conjunto de profesores (no repetidos) que si irán añadiendo conforme se contraten los profesores.

    def __str__(self) -> str:
        profesores_str = [str(profesor) for profesor in self.profesores]
        return f"Lista de profesores en el departamento {self.nombre_dep.name}: {', '.join(profesores_str)}"

class Asignatura:
    def __init__(self, nombre:str, codigo:int, creditos:int) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def __str__(self) -> str:
        return f"Asignatura: {self.nombre}\nCódigo: {self.codigo}\nCréditos: {self.creditos}"
    


