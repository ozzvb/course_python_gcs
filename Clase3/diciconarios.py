colores_casa={ "puerta":"cafe", "pared":"blanco", "piso":"negro"}

print(type(colores_casa))
print( colores_casa["pared"] )
print("-------------------------")

for color in colores_casa :
    print("El color de "+color+" es "+colores_casa[color])

print(  "puerta" in colores_casa  )