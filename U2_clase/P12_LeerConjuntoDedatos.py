nombre_instancia = "../Archivos/Datos_Calificaciones.csv"
archivo = open(nombre_instancia)
contenido_archivo =  archivo.readlines()
print(contenido_archivo)

instancia = [linea.split(",")for  linea in  contenido_archivo]
del instancia[0]
instancia = [[registro[0],int(registro[1])] for registro in instancia]
print(instancia)

instancia.sort(key=lambda  x: x[1] , reverse=True)
print(instancia)

print("Alumnos calificaciones mas altas")
print("Alumno con calificaciones mas altas:" + instancia[0][0])
for i in range(1,len(instancia)):
    calificacion = instancia[i][1]
if instancia[i][1] == calificacion:
    print("Alumno con calificaciones mas bajas:" + instancia [i][0])



