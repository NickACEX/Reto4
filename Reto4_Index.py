#Importamos Funciones
import Reto4_AlProf
#Registrar Alumno
#Parte 1 Ingesta Datos con Lista
try:
    print('Ingrese el Registro de Alumno')
    print(f'¿Ingrese el Nombre del Alumno?')
    nombre=input()#Se ingresa el nombre del alumno
    print(f'¿Ingrese los Apellidos del Alumno?')
    apellidos=input()#Se ingresa los apellidos del alumno
    print(f'¿Ingrese la Edad del Alumno?')
    edad=int(input())#Se ingresa la Edad del alumno
    print(f'¿Ingrese el DNI del Alumno?')
    dni=int(input())#Se ingresa el DNI del alumno
    print('¿Cuantas Notas tiene?')
    numnotas=int(input())#validar si es un numero
    listnota=[]
    for i in range(0,int(numnotas),1):
        print(f'¿Ingrese la Nota numero {i+1}?')
        nota=int(input())#validar si es un numero
        listnota.insert(i, nota)
    
except ValueError as e:
    print(f'Ocurrio un Problema, Solo debes de ingresar numeros')
except Exception as e:
    print(e.__class__.__name__)
    print(f'Ocurrio un Problema : {str(e)}')
finally:
    print('Se termino la ejecucion')

#Parte 2 Nota Mayor
notamayor=int(listnota[1])
for i in listnota:
    if int(i)>=notamayor:
        notamayor=int(i)
print(f'La Nota Mayor es : {notamayor}')

#Parte 3 Nota Menor
notamenor=int(listnota[1])
for i in listnota:
    if int(i)<=notamenor:
        notamenor=int(i)
print(f'La Nota Menor es : {notamenor}')

#Parte 4 Nota Promedio
sumatoria=0
notaprom=0
for i in listnota:
    sumatoria=int(i)+sumatoria
notaprom=sumatoria/int(numnotas)
print(f'El promedio de las Nota es : {notaprom}')

alumnor=Reto4_AlProf.Alumno(nombre,apellidos,edad,dni,listnota,notaprom,notamayor,notamenor)
print (alumnor)
archivo_AL=Reto4_AlProf.RegistroAL('alumnos.txt')
archivo_AL.agregar_alumnos(alumnor)
archivo_AL.listar_alumnos()

#Registrar Profesor
#Parte 1 Ingesta Datos con Lista
try:
    print('Ingrese el Registro de Profesor')
    print(f'¿Ingrese el Nombre del Profesor?')
    nombrep=input()#Se ingresa el nombre del profesor
    print(f'¿Ingrese la Edad del Profesor?')
    edadp=int(input())#Se ingresa la Edad del profesor
    print(f'¿Ingrese el DNI del Profesor?')
    dnip=int(input())#Se ingresa el DNI del profesor
    print(f'¿Ingrese la Materia del Profesor?')
    materiap=input()#Se ingresa la Materia del profesor
    
except ValueError as e:
    print(f'Ocurrio un Problema, Solo debes de ingresar numeros')
except Exception as e:
    print(e.__class__.__name__)
    print(f'Ocurrio un Problema : {str(e)}')
finally:
    print('Se termino la ejecucion')

profer=Reto4_AlProf.Profesor(nombrep,edadp,dnip,materiap)
print (profer)
archivo_AL=Reto4_AlProf.RegistroPROF('profesores.txt')
archivo_AL.agregar_profesores(profer)
archivo_AL.listar_profesores()
