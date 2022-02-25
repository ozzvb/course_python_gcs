for num in range(101) :
    if num != 0 :
        if num == 100 :
            print(num)
        else :
            print(num,end=" - ")
            
print ("----------------------------------")

lista=[ 'casa', 'carro', 'cancho', 30 ]

for x in range(len(lista)) :
    print("El elemento ", x , " de la lista es: ", lista[x])

palabra="Python"
for x in range( len(palabra) ) :
    print( "La letra ", x , "de la palabra es", palabra[x] )
    
