import math
def hipotenusa(a,b):
    if a<0 or b<0:
        raise ValueError('Os lados do triangulo não podem ser negativos')
    return math.sqrt(a**2+b**2)
a=3
b=4
resultado=hipotenusa(a,b)
print(f"a hipotenusa do triangulo com lados {a} e {b} é {resultado}")