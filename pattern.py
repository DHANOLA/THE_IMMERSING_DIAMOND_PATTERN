n=int(input("ENTER THE DEPTH: "))                                                                         #input for the length or the row of blocks

liq=input("ENTER THE LIQUID OF VALUE('.' or ',' or '-' or '_'): ")                                        #input for the column style or pattern

symbol=input("ENTER THE ATOM OF THE ATOMS('*' or 'x' or 'o' or '@'): ")                               #input for the actual diamond or plot made up of or from

down=list()
downer=-1


for i in range(0,(2*n-1)):                                        #loop for the rows counting
    if i<=(2*n-1)%n:
        temp=list()
        for j in range((2*n-1)-(2*i),(2*n-1)+(2*i)+1,2):                                        #loop for the column counting
            temp.append(j)
        down.append(temp)
    else:
        downer-=1


                                        
                                    



upperer=0                     #to start from first element of upper list
downer=-2                     #to start from second last element of down list
lst=0
for i in range(2*n-1,0,-1):                                        #plot the diamond on the basis of coordinates in down list
    count=0
    
    for j in range(4*n-3,0,-1):
        
        if i>=n:                                   #code for the upper half
        
            if j in down[upperer]:
                print(symbol,end='')
                
            else:
                print(liq,end='')                                   #code for the upper half column
            
        
        else:                                   #code for the lower half
            if j in down[downer]:
                print(symbol,end='')
                
            else:
                print(liq,end='')                                   #code for the lower half column
    if i<n:
        downer-=1
    upperer+=1
    
    print("\n")                                   #move to next row
    
