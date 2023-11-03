def base(funcion):
    
    def interna(n1,n2):
        print('Inicia la función base')
        print(funcion(n1,n2))#*        
        #return funcion(n1,n2)
        #funcion(n1,n2)
        print('Finaliza la función base')
    return interna

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

@base
def multiplicar(num1,num2):
    return num1*num2

var1=base(suma)
var2=base(resta)
#var1(10,15)#*
#var2(15,10)#*
var1(10,15)
var2(15,10)
multiplicar(4,8)