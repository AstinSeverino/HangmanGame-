def run ():
    pass
#USANDO FILTER  

# #filter funtion how use
# # es una funcion para filtrar datos como su nombre lo dice 
#     myList = [1,2,3,4,5,6,7,8,9,10,30, 100, 43343] 
# #esto lo que hace es filtrar los datos con esta estrutura usando lamdba funtion y el iterable 
#     filtran =list(filter(lambda i: i%3 !=0 , myList))   
#     print(filtran)

# USANDO MAP 

#     lista =[1,2,45,65,2,2]
#     # scuare = [i**2 for i in lista]
#     # print(scuare)
    
#     filtran2 = list(map(lambda i:i**2, lista)) 
#     print(filtran2)
# #es lo mismo que filter pero en este caso la misma solo se cambia la para filter por map en la estrutura 
# #la funcion map cocinar operaciones como la imagen realiza operaciones (no es para filtar nada) solo realiza proceso 

# usando reduce 

    from functools import reduce

    listita =[2,2,2,2,2]

    listitaFinal2 = reduce(lambda i, i2: i * i2, listita)
    print(listitaFinal2)
# aqui esta reduce es una funcion que reduce los datos que estan dentro de un array y nos permite hacer opercaciones con los mismos
# que obtenemos un producto final de la lista con el valor de los datos 
    # listitaFinal = 1
    # for i in listita:
    #     listitaFinal = listitaFinal * i
    #     print(listitaFinal)


if __name__=='__main__':
  run()