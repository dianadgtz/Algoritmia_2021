import random

def repaso(nombre, num_preguntas):
    aciertos = 0
    operaciones = ["+", "-", "*", "/"]

    for i in range(num_preguntas):
        a = random.randint(1,9)
        b = random.randint(1,9)
        oper = random.randint(0,3)


        resultado = input(f"{a}{}{b} =")

        if validar(a, b, operaciones[oper], resultado):
            aciertos += 1
  


    print(f"{nombre} ha conseguido {aciertos}/{num_preguntas}")


# Funcion a terminar
def validar(a, b, operador, c):  # 4, 5, '*', 20    | 1,3, '/', 0 | + | -
    """[validar una operación]

    Args:
        a (int): [cualquier nmero]
        b (int): [cualquier numero]
        operador (string): [operacion]
    Returns:
        c (float): [resultado]
    """
    print("resultados")
    return [a+b, a-b, a*b, a/b]
    
    if operador == '+':
        if (a + b) == c:
            return True
        else:
            return False
            

    return False 
resultados = validar (4, 5, '+', 9)
resultados = validar (1, 3, '/', 1/3)



if __name__ == '__main__':
    repaso("Arturo", 3)