from sistema_universidad import *
import pytest
'''Aclaración: hago as pruebas para los métodos qeu considero necesarios, hay algunos que no me hacen falta por lo breve que es el método'''


'''Comenzamos las pruebas para la clase Universidad'''
universidad = Universidad()

# Creamos algunos profesores y alumnos para utilizar en las pruebas
profesor1 = Profesor("Juan", "23303508T", "Calle 123", "H")
profesor2 = Profesor("Maria", "23303508T", "Calle 456", "M")
alumno1 = Estudiante(1, "Pedro", "23303508T", "Calle 789", "H")
alumno2 = Estudiante(2, "Ana", "23303508T", "Calle 012", "M")

# Agregamos los profesores y alumnos creados a la lista de la universidad
universidad.listado_profesores.append(profesor1)
universidad.listado_profesores.append(profesor2)
universidad.listado_alumnos.append(alumno1)
universidad.listado_alumnos.append(alumno2)

def test_obtener_profesor_existente():
    # El profesor si tiene que existir en la lista
    assert universidad.obtener_profesor("23303508T") == profesor1

def test_obtener_profesor_inexistente():
    # El profesor no tiene que existir en la lista
    assert universidad.obtener_profesor("34567299Z") is None

def test_obtener_alumno_inexistente():
    # El alumno no tiene que existir en la lista
    assert universidad.obtener_alumno("12345678Z") is None


def test_DarBaja_alumno_existente():
    # alumno existe en la lista alumnos
    universidad.DarBaja_alumno(1, "Pedro", "23303508T", "Calle 789", "H")
    assert alumno1 not in universidad.listado_alumnos

def test_graduar_alumno_creditos_suficientes():
    # Probamos el caso donde el alumno tiene suficientes créditos para graduarse
    universidad.graduar_alumno(1, "Pedro", "23303508T", "Calle 789", "H")
    assert alumno1 not in universidad.listado_alumnos

def test_graduar_alumno_creditos_insuficientes(capsys):
    # Probamos el caso donde el alumno no tiene suficientes créditos para graduarse
    universidad.graduar_alumno(2, "Ana", "23303508T", "Calle 012", "M")
    captured = capsys.readouterr()
    assert "Créditos insuficientes\n" == captured.out

def test_despedir_profesor_inexistente(capsys):
    # Probamos el caso donde el profesor no existe en la lista
    universidad.despedir_profesor("Pedro", "33333333Z", "Calle 456", "M", titular=True)
    captured = capsys.readouterr()
    assert "No se ha encontrado al profesor con DNI: 33333333Z\n" == captured.out

def test_jubilar_profesor_inexistente(capsys):
    universidad.jubilar_profesor("Juan", "33333333Z", "Calle 456", "M", titular=False)
    captured = capsys.readouterr()
    assert "No se ha encontrado al profesor con DNI: 33333333Z\n" == captured.out

def test_actualizar_datos_estudiante_inexistente(capsys):
    # Probamos el caso donde el estudiante no existe en la lista
    universidad.actualizar_datos_estudiante("12345678A", nombre="Luisa", direccion="Calle 789", sexo="F", curso=3, creditos=150)
    captured = capsys.readouterr()
    assert "No se ha encontrado al estudiante con DNI: 12345678A\n" == captured.out

def test_actualizar_datos_profesor_inexistente(capsys):
    # Probamos el caso donde el profesor no existe en la lista
    universidad.actualizar_datos_profesor("23456789P", nombre="Laura", direccion="Calle 789", sexo="F", trabajo_externo="Cloud Computing")
    captured = capsys.readouterr()
    assert "No se ha encontrado al profesor con DNI: 23456789P\n" == captured.out

'''Pruebas clase Persona'''
persona1 = Persona('Juan', '23303508T', 'calle Greco, Nº 4, ciudad5', 'H')

def test_validar_identidad_dni_correcto():
    assert persona1.validar_identidad("23303508T") == True
#Lo importante es comprobar para una letra incorrecta
def test_validar_identidad_dni_letra_incorrecta():
    assert persona1.validar_identidad("23303508A") == False

#Lo compruebo para la letra X pero sería lo mismo con el resto:
def test_validar_identidad_nie_correcto_letra_x():
    assert persona1.validar_identidad("X6523796F") == True

def test_validar_identidad_nie_letra_incorrecta():
    assert persona1.validar_identidad("X1234567A") == False

'''Pruebas clase Estudiante(SIMILAR A LOS METODOS DE LA CLASE PROFESOR)'''
estudiante1 = Estudiante(1, "Pedro", "23303508T", "Calle 789", "H")

def test_matricular_asignatura():
    asignatura = Asignatura("Matemáticas", 101, 6)
    estudiante1.matricular_asignaturas(asignatura)
    assert len(estudiante1.lista_asignaturas) == 1
    assert estudiante1.lista_asignaturas[0] == asignatura

def test_aprobar_asignatura_inexistente():
    asignatura = Asignatura("Matemáticas", 101, 4)
    with pytest.raises(ValueError):
        estudiante1.aprobar_asignatura(asignatura)
