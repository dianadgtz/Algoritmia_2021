def operaciones(a=1, b=1) -> list:
    """[Realiza todas las operaciones]
    Args:
        a (int, optional): [description]. Defaults to 1.
        b (int, optional): [description]. Defaults to 1.
    Returns:
        [int, float]: [description]
    """
    print("Proceso terminado")
    return [a+b, a-b, a*b, a/b]


def despedida(nombre):
    saludo(nombre)
    print(f"Adios {nombre}")


def saludo(nombre):
    print(f"Hola {nombre}")




A = operaciones(4, 2) 
despedida("Juan")
