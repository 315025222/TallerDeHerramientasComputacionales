alumnos = []
alumnos.append([9, 8, 10, 9])
alumnos.append([9])
alumnos.append([6, 9, 10, 10 ,9])


def mostrarAlumnos(listaA):
    contador = 1
    print("Las calificaciones aprobatorias de los alumnos son:")
    for i in listaA:
        impresion = ""
        alumno = "alumno #%d:    " % contador

        for j in i:
            impresion += str(j) + "    "
        print(alumno + impresion)
        contador += 1


mostrarAlumnos(alumnos)
