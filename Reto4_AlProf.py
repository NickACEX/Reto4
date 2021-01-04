#Registro de Alumnos ,Notas y Profesor
class Alumno:
    #Atributos del Alumno
    def __init__(self, nombre,apellidos,edad,dni,notas,promedio,nota_maxima,nota_minima):
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.dni=dni
        self.notas=notas
        self.promedio=promedio
        self.nota_maxima=nota_maxima
        self.nota_minima=nota_minima

class Profesor:
    #Atributos del Profesor
    def __init__(self, nombre,edad,dni,materia):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.materia=materia

class RegistroAL:
    #Atributos del Registro de Alumno
    def __init__(self, nombre_archivo_AL):
        self.nombre_archivo_AL=nombre_archivo_AL

    def listar_alumnos(self):
        try:
            file=open(self.nombre_archivo_AL, 'r') 
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            if(file):
                file.close()

    def agregar_alumnos(self, Alumno):
        try:
            file=open(self.nombre_archivo_AL, 'a')
            text_alumno=f'{Alumno.nombre},{Alumno.apellidos},{Alumno.edad},{Alumno.dni},{Alumno.notas},{Alumno.promedio},{Alumno.nota_maxima},{Alumno.nota_minima}' 
            file.write(text_alumno)
            file.write('\n')
        except Exception as e:
            print(f'Error:{e}')
        finally:
            if(file):
                file.close()

class RegistroPROF:
    #Atributos del Registro de Profesor
    def __init__(self, nombre_archivo_PROF):
        self.nombre_archivo_PROF=nombre_archivo_PROF

    def listar_profesores(self):
        try:
            file=open(self.nombre_archivo_PROF, 'r') 
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            if(file):
                file.close()

    def agregar_profesores(self, Profesor):
        try:
            file=open(self.nombre_archivo_PROF, 'a')
            text_profesor=f'{Profesor.nombre},{Profesor.edad},{Profesor.dni},{Profesor.materia}' 
            file.write(text_profesor)
            file.write('\n')
        except Exception as e:
            print(f'Error:{e}')
        finally:
            if(file):
                file.close()
