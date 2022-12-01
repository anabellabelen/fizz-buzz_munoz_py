def fizz_buzz(numb):             #Defini la funcion, creando numb como elemento
    for i in range(1,numb+1):    # Utilizo el for para comenzar un contador, poniendo i como variable, y creo el rango
        if i % 15==0:            #Utilizo if para iniciar la comparacion de i con %(division) por 15( 3x5=15) y lo coloco primero poorque sino toma el primer parametro que ponca ya sea fizz o buzz
            print(i,"Fizz Buzz") #Imprimo el numero que esta contando, mas Fizz Buzz que daria el parametro al ser divisible por 3 y 5
        elif i % 3==0:           #Utilizo elif para iniciar la segunda comparacion de i, siendo esta solo divisible por 3
            print(i,"Fizz")      #Imprimo el numero mas Fizz, que daria el segundo parametro establecido por el ejercisio
        elif i % 5==0:           #Nuevamente utilizo elif para comparar i, esta vez siendo divisible por 5 solamente
            print(i,"Buzz")      #Imprimo el numero mas la palabra Buzz como pedia el ultimo parametro de nuestro ejercisio
        else:                    #Utilizo para cerrar el ejerciso un else(son todos los valores que quedan fuera de los parametros del ejercisio)
            print(i)             #Imprimo el valor de estos numeros
fizz_buzz(100)                   #Pongo el tope del rango de la funcion for(siendo este modificable cambiando el parentesis)