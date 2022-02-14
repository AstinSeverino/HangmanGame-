def run ():
    pass
#filter funtion how use
# es una funcion para filtrar datos como su nombre lo dice 
    myList = [1,2,3,4,5,6,7,8,9,10,30, 100, 43343] 
#esto lo que hace es filtrar los datos con esta estrutura usando lamdba funtion y el iterable 
    filtran =list(filter(lambda i: i%3 !=0 , myList))   
    print(filtran)

if __name__=='__main__':
  run()