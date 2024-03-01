#===================================
#===================================
# Name   : 
# Roll no: 
# Section: 
# Date   : 20-02-2023
#===================================
#===================================

#===================================
#  Function for Task 1.3.1.1
#===================================
def F1311():
    """
    Output:
        --> Write your output here
    """
    # Replace with your own code:
    print(16+4//2-10)
    
    
#===================================
#  Function for Task 1.3.2.1
#===================================
def F1321(a,b):
    # Replace the blank with your own boolean statement:
    if a%b==0:
        return True
    else:
        return False
    
    
#===================================
#  Function for Task 1.3.2.2
#===================================
def F1322():
    """
    Output:
        --> Write your output here
    """
    # Replace with your own code:
    print(4 > 5)
    print(4 < 5)
    print(4 <= 5)
    print(4 == 5)
    print(2 >= 1)
    print(1 != 1)
    print(-1 < 0)
    print(4 < 5 and 10 > 9)
    print(True or False)



#===================================
#  Function for Task 1.3.4.1
#===================================
def F1341():
    # Replace with your own code:
    print(10 - 4 * 2)
    print(10 - (4 * 2))
    print((10 - 4) * 2)

    
    
#===================================
#  Function for Task 1.4.1.1
#===================================
def F1411(score):
    # Replace with your own code:
    if score>=90:
        return 'Good'
    if score>=60:
        return 'pass'
    
    if score<60:
        return 'fail'
    
#===================================

#  Function for Task 1.4.1.2
#===================================
def F1412(n):
    for a in range(n):
        print('*'*(a+1))

    # Replace with your own code:
    



#===================================
#  Function for Task 1.4.1.3
#===================================    
def F1413(n):
    a = 0
    while a!=n:
        print('*'*(a+1))
        a+=1
    # Replace with your own code:
    
    

#===================================
#  Function for Task 1.4.1.4
#===================================
def F1414():
    '''
    - Continue / skip the current iteration if i is either 6 or 23
    - Break the loop if i is 7
    '''
    sum = 0
    for i in range(2,36):
        
        sum += i
    return sum
    


#===================================
#  Function for Task 1.5.1.1
#===================================    
def F1511(a,b):
    """
    Add two numbers here and return the output
    Parameters:
        a: Integer
        b: Integer
    Return value:
        square of the sum of a and b
    """
    # Replace with your own code:
    return (a+b)


#===================================
#  Function for Task 1.5.1.1
#===================================    
def F1512(C):
    # Replace with your own code:
    return (C*9/5)+32



#===================================
#  Function for Task 1.5.1.3
#===================================    
def F1513(n):
    # Replace with your own code:
    if n == 1:
        return n
    else:
        return n*F1513(n-1)


#===================================
#  Function for Task 1.5.1.4
#===================================    
def F1514(a,b,c):
    """
    find average of three numbers: a,b,c
    """
    # Replace with your own code:
    return (a+b+c)/3



#===================================
#  Function for Task 1.6.1.1
#===================================
def F1611():
    '''
    Some useful information here
    expected input:
        None
    expected output:
        --> write your expected output here
    '''
    # Replace with your own code:
    print('hello')
    print('world')
       
  

#===================================
#  Function for Task 1.6.1.2
#===================================
def F1612():
   
    print( '''               ***************
                   comp200
               ****************
                                   ''')


  
#===================================
#  Function for Task 1.6.1.3
#===================================
def F1613():
    name = "Ali"
    gpa = 3.23534
    print(f'my name is {name} and gpa is {gpa}' )
    
   
   
   
#===================================
#  Function for Task 1.6.1.4
#===================================
def F1614(sum, avg):
    print(f'sum: {sum}--- average: {avg}')
   
   
   
#===================================
#  Function for Task 1.6.1.5
#===================================
def F1615(n):
    count = 0
    total =0
    while count!=n:
        
        numb = int(input('Enter: '))
        total+=numb
        count+=1
        if count ==n:
            print(total)
        
        
    
    
#===================================
#  Function for Task 1.6.2.1
#===================================
def F1621():
    '''
    Some useful information here
    expected input:
        None
    expected output:
        --> File name called data.txt containing 5 numbers 
             from 0-4 each in a new line
    '''
    # Replace with your own code:
    raise NotImplementedError


#===================================
#  Function for Task 1.6.2.2
#===================================
def F1622():
    '''
    Some useful information here
    expected input:
        None
    expected output:
        --> Sum of n numbers stored in the file "input.txt"
    '''
    # Replace with your own code:
    raise NotImplementedError
  
#=========================================

