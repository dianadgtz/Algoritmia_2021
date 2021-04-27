class Person:
    '''Clase de Persona
    recibe el nombre y apellido como parametro'''
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname , lname)
        self.__carrera = 'medicina'
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setClave(esta, clave):
        esta.__clave = clave

    def getCarrera(self):
        return self.__carrera 

    def setCarrera(esta, carrera):
        esta.__carrera = 'psicologia'

    def printname(self):
        super().printname()
        print("Soy estudiante")

Alejandra = Person('Alejandra', 'Pinos')
Alejandra.printname()
print()
Alexis = Student('Alexis', 'Cruz', 200293)
Alexis.printname()
print('Mi clave es:', Alexis.getClave())
print('Mi carrera es:', Alexis.getCarrera())
print()
Alondra = Student('Alondra', 'Mejia', 178538)
Alondra.printname()
Alondra.setClave(188538)
print('Mi clave es:', Alondra.getClave())
Alondra.setCarrera('Picología')
print('Mi carrera es:', Alondra.getCarrera())