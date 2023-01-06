def convertirEnteroABase(numero, base):
    conversionCadena = '0123456789ABCDEF'

    if numero < base:
        return conversionCadena[numero]
    else:
        return convertirEnteroABase(numero//base, base) + conversionCadena[numero % base]

n=int(input("Ingrese un numero entero: "))
p=int(input("Ingrese a la base que quiere cambiar el numero: "))
resultado = convertirEnteroABase(n, p)
print(resultado)