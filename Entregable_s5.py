def datos(Nombre, ApellidoPaterno, ApellidoMaterno, clave, salon):
    datos = {}
    print(f"Este es mi nombre completo: {Nombre} {ApellidoPaterno} {ApellidoMaterno}")
    print(f"Esta es mi clave ULSA: {clave}") 
    print(f"Este es mi salón: {salon}")
    return datos
datos("Diana", "Delgado", "Gutierrez", "200293", "292")

