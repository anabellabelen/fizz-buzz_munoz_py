def fizz_buzz(numb):             
    for i in range(1,numb+1):    
        if i % 15==0:            
            print(i,"Fizz Buzz") 
        elif i % 3==0:           
            print(i,"Fizz")      
        elif i % 5==0:           
            print(i,"Buzz")     
        else:                    
            print(i)             
fizz_buzz(100)                   
