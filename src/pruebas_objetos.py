# Importo todas las clases desde el archivo sistema_universidad
from sistema_universidad import *

'''Creación de objetos'''
#PRIMERA CREACIÓN ANTES DE AÑADIR LOS MÉTODOS CORRESPONDIENTES A CADA CLASE

# Creacion de objetos Persona:
'''Esta clase no es necesaria de usarla como ejemplo para el caso de los estudiantes y profesores
sin mebargo, se puede usar como una clase base de personas con otros oficios dentro de la universidad, aunque
yo sólo la utilizaré para caso de profesores y estudiantes. '''

persona1 = Persona('Juan', '23303508H', 'calle Greco, Nº 4, ciudad5', 'H')
persona2 = Persona('Teresa', '23302408L', 'calle Luco, nº 3, ciudad7', 'M')
persona3 = Persona('Pablo', '23309008B', 'calle Polo, nº 47, ciudad9', 'H')
persona4 = Persona('Juan', '23309938I', 'calle Azul, nº 12, ciudad23', 'M')
print(persona1)

# Creación de objetos Profesor:
''''Explicación de la clase Profesor'''

'''Es cierto que el objetivo del enunciado solo menciona a los profesores titulares y asociados,
sin embargo, puede haber diferentes tipos de profesores además de los profesores titulares o asociados.
Por ejemplo, se puede tener profesores visitantes, profesores adjuntos, etc.
Por ello, si tiene sentido tener una clase base Profesor de la cual puedan heredar los diferentes
tipos de profesores, como ProfesorTitular, ProfesorAsociado u otros no mencionados en el documento'''

profesor1 = Profesor(['Matematicas II', 'Deep Learning', 'Base de datos I'],
                    18, EDep.DIIC,
                    'Raúl López' ,
                    '28477654V',
                    'Calle Puerto nº 2, Ciudad4',
                    'H')

profesor2 = Profesor(['Matematicas I', 'Deep Learning', 'Base de datos II'],
                    18,
                    EDep.DIIC,
                    'David Pérez' ,
                    '28477394T',
                    'Calle Venus nº 21, Ciudad3',
                    'H')

profesor3 = Profesor(['Calculo II', 'Teoría  de la Señal', 'Algebra'],
                    18,
                    EDep.DIIC,
                    'Isabel Díaz' ,
                    '28777394H',
                    'Calle Lagos nº 44, Ciudad 43',
                    'M')
print(profesor1)

# Creación de objeto Profesor Titular:
profesor_titular1 = ProfesorTitular(
    area_investigacion="Física",
    asignaturas=["Matematicas II", "Mecánica"],
    creditos=12,
    departamento=EDep.DIS,
    nombre="María Rodríguez",
    DNI="87654321B",
    direccion="Calle BM, Ciudad 1",
    sexo="F")

print("Profesor Titular:")
print("Nombre:", profesor_titular1.nombre)
print("Departamento:", profesor_titular1.departamento)
print("Área de Investigación:", profesor_titular1.area_investigacion)
print("Asignaturas:", profesor_titular1.asignaturas)
print("Créditos:", profesor_titular1.creditos)
print("DNI:", profesor_titular1.DNI)
print("Dirección:", profesor_titular1.direccion)
print("Sexo:", profesor_titular1.sexo)

# Creación de objeto Profesor Asociado:
profesor_asociado1 = ProfesorAsociado(
    trabajo_externo="Diseñador de software",
    asignaturas=["Diseño de Algortimos", "Base de Datos I" ],
    creditos=15,
    departamento=EDep.DITEC,
    nombre="Pedro González",
    DNI="56789123C",
    direccion="Calle C, Ciudad44",
    sexo="M")

print("Profesor Asociado:")
print("Nombre:", profesor_asociado1.nombre)
print("Departamento:", profesor_asociado1.departamento)
print("Trabajo Externo:", profesor_asociado1.trabajo_externo)
print("Asignaturas:", profesor_asociado1.asignaturas)
print("Créditos:", profesor_asociado1.creditos)
print("DNI:", profesor_asociado1.DNI)
print("Dirección:", profesor_asociado1.direccion)
print("Sexo:", profesor_asociado1.sexo)

# Creación de objetos Asignatura:
asignatura1 = Asignatura(nombre="Matemáticas I", creditos=6)
asignatura2 = Asignatura(nombre="Matemáticas II", creditos=6)
asignatura3 = Asignatura(nombre="Computadores", creditos=6)

# Creación de objetos Estudiante:
'''Aclaración con respecto a la creación de asignatura:
    Al haber creado los objetos asignaturas lso utilizo directamente para
    la creación del objeto estudiante
'''
estudiante1 = Estudiante(
    curso="Segundo",
    creditos=40,
    num_expediente="123456",
    asignaturas=[asignatura1.nombre, asignatura2.nombre],
    nombre="Laura López",
    DNI="98799432X",
    direccion="Calle D, Ciudad",
    sexo="F"
)

print("\nEstudiante:")
print("Nombre:", estudiante1.nombre)
print("Curso:", estudiante1.curso)
print("Créditos:", estudiante1.creditos)
print("Número de Expediente:", estudiante1.num_expediente)
print("Asignaturas:", estudiante1.asignaturas)
print("DNI:", estudiante1.DNI)
print("Dirección:", estudiante1.direccion)
print("Sexo:", estudiante1.sexo)


# Creación de objetos Departamento:
departamento1 = Departamento(nombre_dep=EDep.DIIC)
departamento2 = Departamento(nombre_dep=EDep.DITEC)
departamento3 = Departamento(nombre_dep=EDep.DIS)

#departamento1.profesores.add(profesor1)
departamento1.profesores.add(profesor2)

#departamento2.profesores.add(profesor3)
departamento2.profesores.add(profesor_asociado1)
print(departamento1)
print(departamento2)


# Creación objeto Universidad:
'''Esta clase está hecha para facilitar las funcionalidades en cuanto a la
 administracion de las personas de la universidad correspondiente'''


universidad_upct = Universidad()
universidad_upct.matricular_alumno(estudiante1)
print(len(universidad_upct.listado_alumnos))
universidad_upct.contratar_profesor(profesor1)
