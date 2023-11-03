import requests
url= 'http://gutendex.com/books/'
response= requests.get(url)
diccionario=response.json() #resultado del archivo json convertido a objeto en python, un objeto en python es un diccionario

resultados=diccionario['results'] #coge una clave llamada result y queda guardado en resultados 
#print(type(resultados)) #muestra el tipo de dato
#print(len(resultados)) #muestra la cantidad de datos 
#print(type(resultados[0])) #tipo de dato de la posiion 0
#print(resultados[0]) #muestra el resultado
#for key in resultados[0]: #imprime solo las claves 
    #print(key)

#for libro in resultados:
  #for key,  value in libro.items(): #muetra todos los libros 
     #print(f'{key} : {value}')

#titulos
titulos=[libro['title'] for libro in resultados]
titulo=sorted(titulos)

for titulos in titulo:  
  print(titulos)




