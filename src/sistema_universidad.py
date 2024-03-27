from enum import Enum

class Universidad:
    # constructor
    def __init__(self) -> None:
        self.listado_alumnos = []
        self.listado_profesores = []

    def matricular_alumno(self, alumno):
        self.listado_alumnos.append(alumno)
    
    def contratar_profesor(self, profesor):
        self.listado_profesores.append(profesor)

class Persona:
    def __init__(self, nombre:str, DNI:str, direccion:str, sexo:str) -> None:
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.sexo = sexo

    def __str__(self) -> str:
        return  'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion  
 
 
class Profesor(Persona):
    def __init__(self, asignaturas: list, creditos:int, departamento, nombre, DNI, direccion, sexo) -> None:
        # Herencia
        super().__init__(nombre, DNI, direccion, sexo)

        self.asignaturas = asignaturas
        self.creditos = creditos
        self.departamento = departamento

    def __str__(self) -> str:
        return 'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion  

class ProfesorTitular(Profesor):
    def __init__(self, area_investigacion, asignaturas, creditos, departamento, nombre, DNI, direccion, sexo) -> None:
        super().__init__(asignaturas, creditos, departamento, nombre, DNI, direccion, sexo)
        self.area_investigacion = area_investigacion

class ProfesorAsociado(Profesor):
    def __init__(self, trabajo_externo, asignaturas, creditos, departamento, nombre, DNI, direccion, sexo) -> None:
        super().__init__(asignaturas, creditos, departamento, nombre, DNI, direccion, sexo)
        self.trabajo_externo = trabajo_externo

    


class Estudiante(Persona):
    def __init__(self, curso, creditos:int, num_expediente:int, asignaturas:list, nombre, DNI, direccion, sexo) -> None:
        
        super().__init__(nombre, DNI, direccion, sexo)
        self.curso = curso     # el curso corresponderá al curso del cuál esté matriculado con más asignaturas
        self.creditos = creditos
        self.num_expediente = num_expediente
        self.asignaturas = asignaturas

    def __str__(self) -> str:
        return 'nombre: ' + self.nombre + '\n' + 'Género: ' + self.sexo + '\n' + 'Nº Expediente: ' + self.num_expediente + '\n' + 'DNI: '+ self.DNI + '\n' + 'Dirección: ' + self.direccion + '\n' + 'Curso de más creditos matriculado: ' + self.curso +'\n' +  'Creditos: ' + str(self.creditos) +'\n' +  'Asignaturas matriculado: ' + self.asignaturas


class EDep(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3


class Departamento:
    def __init__(self, nombre_dep:EDep) -> None:
        self.nombre_dep = nombre_dep
        self.profesores = set() # Un conjunto de profesores (no repetidos) que si irán añadiendo conforme se contraten los profesores.

    def __str__(self) -> str:
        profesores_str = [str(profesor) for profesor in self.profesores]
        return f"Lista de profesores en el departamento {self.nombre_dep.name}: {', '.join(profesores_str)}"



class Asignatura:
    def __init__(self, nombre, creditos) -> None:
        self.nombre = nombre
        self.creditos = creditos





