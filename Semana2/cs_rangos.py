try :
    salario = int(input("Por favor introduzca el salario para calcular sus cargar sociales: \n"))
    # Revisamos cuanto se debe agregar de carga social:
    if salario > 1000000 :
        carga_social = float(0.3) #float es para decirle a la computadora que va a usar un numero flotante 0.00
    elif salario >= 500000 and salario < 100000 :
        carga_social = float(0.2)
    else : 
        carga_social = float(0.1)

    # Imprimimos el resultado
    print("\n\nCon la carga social de ", ( carga_social*100 ), "% para un salario de ", (salario) ,"\nel importe addicional sería:", (salario*carga_social) ,".", 
        "\nTotal de salario tomando en cuenta las cargas sociales es de ", ((salario*carga_social)+salario  ))
except :
    print( "Algo salio mal, por favor verifique que el valor ingresado corresponde a un valor numerico")