alumnos = []
alumnos.append([9, 8, 10, 9])
alumnos.append([9])
alumnos.append([6, 9, 10, 10, 9])


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


mostrarAlumnos(alumnos)

elsemestre1 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre2 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre3 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre4 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre5 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre6 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre7 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elsemestre8 = [[["algebra"], [9, 3, 10, 8], [9, 7, 10, 8], [15], [9]],
               [["geometria"], [9, 9, 6, 8], [9, 3, 10, 8], [16], [8]],
               [["calculo"], [1, 5, 10, 8], [9, 8, 5, 8], [9], [6]]]

elhistorial = []
elhistorial.append(elsemestre1)
elhistorial.append(elsemestre2)
elhistorial.append(elsemestre3)
elhistorial.append(elsemestre4)
elhistorial.append(elsemestre5)
elhistorial.append(elsemestre6)
elhistorial.append(elsemestre7)
elhistorial.append(elsemestre8)


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


mostrarHistorial(elhistorial)
