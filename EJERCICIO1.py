n=int(input("Ingrese un numero: "))
p=int(input("Ingrese otro numero: "))
 
def sumatoria(n,p,acumulado):
  while n>0 :
    acumulado += n*p
    n -= 1    
  return acumulado
 
print("La funcion k(",n,",",p,"):es: ",sumatoria(n,p,0))