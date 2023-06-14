def control(op,num,num2):
        #print (op)
        if op == "1":
            res=num+num2
            #print ("Suma es:",res)
        elif op == "2":
            res=num-num2
            #print ("Resta es:",res)
        elif op == "3":
            res=num*num2
            #print ("3.-multiplicacion es:",res)
        elif op == "4":
            if num2==0:
                #pass    #la instruccion pass permite un break en bucles anidados elif
                #break continue y pass son instrucciones de simular un switch para python
                res=0
                print ("division entre zero-segundo numero no puede ser cero") #si no quieres mensaje usas pass
            else:
                res=num/num2
                #print ("4.-Division:",res)
        elif op == "5":
            res=0
            print ("Salir del Programa")
       
        elif op > "5" :
             res=0
             
    
        return (res)
