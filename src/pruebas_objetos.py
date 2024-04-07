# Importo todas las clases desde el archivo sistema_universidad
from sistema_universidad import *

'''Creación de objetos individuales'''
import random

def generar_dni():
    numeros = ''.join(random.choices('0123456789', k=8))
    letras = random.choice('TRWAGMYFPDXBNJZSQVHLCKE')
    return str(numeros + letras)

# Creacion de objeto Persona:
'''Esta clase no es necesaria de usarla como ejemplo para el caso de los estudiantes y profesores
sin mebargo, se puede usar como una clase base de personas con otros oficios dentro de la universidad, aunque
yo sólo la utilizaré para caso de profesores y estudiantes. '''

persona1 = Persona('Juan', '23303508T', 'calle Greco, Nº 4, ciudad5', 'H')
print(persona1)

# Creación de objetos Profesor:
''''Explicación de la clase Profesor'''

'''Es cierto que el objetivo del enunciado solo menciona a los profesores titulares y asociados,
sin embargo, puede haber diferentes tipos de profesores además de los profesores titulares o asociados.
Por ejemplo, se puede tener profesores visitantes, profesores adjuntos, etc.
Por ello, si tiene sentido tener una clase base Profesor de la cual puedan heredar los diferentes
tipos de profesores, como ProfesorTitular, ProfesorAsociado u otros no mencionados en el documento'''

profesor1 = Profesor(
                    'Raúl López' ,
                    '23303508T',
                    'Calle Puerto nº 2, Ciudad4',
                    'H')

print(profesor1)

# Creación de objeto Profesor Titular:
profesor_titular1 = ProfesorTitular(
    area_investigacion="Física",
    nombre="María Rodríguez",
    DNI="23303508T",
    direccion="Calle BM, Ciudad 1",
    sexo="M")
print(profesor_titular1)

# Creación de objeto Profesor Asociado:
profesor_asociado1 = ProfesorAsociado(
    trabajo_externo="Diseñador de software",
    nombre="Pedro González",
    DNI='23303508T',
    direccion="Calle C, Ciudad44",
    sexo="H")

print(profesor_asociado1)

# Creación de objetos Asignatura:
asignatura1 = Asignatura(nombre="Matemáticas I", codigo=1234, creditos=6)
asignatura2 = Asignatura(nombre="Matemáticas II", codigo=2345, creditos=6)
asignatura3 = Asignatura(nombre="Computadores", codigo=4567, creditos=6)

print(asignatura1)

# Creación de objetos Estudiante:
'''Aclaración con respecto a la creación de asignatura:
    Al haber creado los objetos asignaturas los utilizo directamente para
    la creación del objeto estudiante
'''
estudiante1 = Estudiante(
    curso=2,
    nombre="Laura López",
    DNI="23303508T",
    direccion="Calle D, Ciudad",
    sexo="M")

print(estudiante1)


# Creación de objetos Departamento:
departamento1 = Departamento(nombre_dep=EDep.DIIC)
departamento2 = Departamento(nombre_dep=EDep.DITEC)
departamento3 = Departamento(nombre_dep=EDep.DIS)

print(departamento1)
print(departamento2)


# Creación objeto Universidad:
'''Esta clase está hecha para facilitar las funcionalidades en cuanto a la
 administracion de las personas de la universidad correspondiente'''

universidad_upct = Universidad()


'''Uso de métodos de las clases'''
# comenzamos por la clase Universidad:

universidad_upct.añadir_asignatura("Matemáticas", 2344, 6)
universidad_upct.añadir_asignatura("Base de Datos", 2364, 6)

universidad_upct.matricular_alumno(1, 'Laura', '23303508T', 'Calle 2033', 'M')

universidad_upct.contratar_profesor('Paco', '23303508T', 'calle azul', 'H', True)

print(universidad_upct.obtener_alumno('23303508T'))
print(universidad_upct.obtener_profesor('23303508T'))

universidad_upct.DarBaja_alumno(1, 'Laura', '23303500T', 'Calle 2033', 'M')
universidad_upct.graduar_alumno(1, 'Laura', '23303508T', 'Calle 2033', 'M')

universidad_upct.despedir_profesor('Paco', '23303508T', 'calle azul', 'H', True)
universidad_upct.jubilar_profesor('Paco', '23303508T', 'calle azul', 'H', True)


universidad_upct.matricular_alumno(1, 'Laura', '23303508T', 'Calle 2033', 'M')

universidad_upct.contratar_profesor('Paco', '23303508T', 'calle azul', 'H', True)

universidad_upct.actualizar_datos_profesor("23303508T", nombre="Pedro Rodríguez", direccion="Avenida 456")

universidad_upct.actualizar_datos_estudiante("23303508T", nombre="María Gómez")

# Métodos de la clase Persona:
# El más importante es el metodo validar identidad ya que un DNI es único e imprescindible para una persona
# Además también se considera el NIE
persona= Persona('dana', 'X6523796F', 'Calle 2nef', 'M')

'DNI no válido salta excepción:'
#persona = Persona('Brandon', '23858338H', 'Calle azul', 'H')

# Métodos clase Profesor(Titular o Asociado):
'VOy a añadir una asignatura al profesor creado antes:'
profesor_titular1.asignar_asignatura(asignatura2)
profesor_asociado1.asignar_asignatura(asignatura1)
print(22222222222222222222222222)
profesor_titular1.cambiar_areaIVN = 'FLORA'
profesor_titular1.asignar_departamento(EDep.DIIC)
print(profesor_titular1.departamento)
print(profesor_titular1)
print(profesor_asociado1)


# Metodos clase Estudiante
estudiante2 = Estudiante(
    curso="Primero",
    nombre="Manuel Núñez",
    DNI="23303508T",
    direccion="Calle p, Ciudad22",
    sexo="H")
estudiante2.matricular_asignaturas(asignatura1)
estudiante2.aprobar_asignatura(asignatura1) #se debe de sumar 6 por laasignatura aprobada
print(estudiante2)
