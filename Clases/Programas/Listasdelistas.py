def mostrarAlumnos(listaA):
    contador = 1
    print("Las calificaciones aprobatorias de los alumnos son:")
    for sublista in listaA:
        impresion = ""
        alumno = "alumno #%d:    " % contador

        for valor in sublista:
            impresion += str(valor) + "    "
        print(alumno + impresion)
        contador += 1


def desplegar(sublista):
    impresion = ""
    for valor in sublista:
        impresion += str(valor) + "    "
    return impresion


def mostrarSemestre(semestre):
    for i in semestre:
        examenes = desplegar(i[1])
        tareas = desplegar(i[2])
        print("Materia: %s" % i[0][0])
        print("Exámenes: {}".format(examenes))
        print("Tareas: {}".format(tareas))
        print("Asistencias: {}".format(i[3][0]))
        print("Calificación final: {} \n".format(i[4][0]))



def mostrarHistorial(historial):
    contador = 1
    for semestron in historial:
        print("Los resultados del semestre %d son:" % contador)
        mostrarSemestre(semestron)
        contador += 1
        print("=" * 100)


