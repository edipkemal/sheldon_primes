def isPrime(number):
    if number<2:
        return 0
    for i in range(2,number):
        if number%i==0:
            return 0
    return 1

def digitMultiplication(number):
    
    result=1
    while(number!=0):
        kalan=number%10
        number-=kalan
        number=number/10
        result*=kalan
        
    return result

def getMirror(number):
    str_number=str(number)
    new_str=""
    for i in range(1,len(str_number)+1):
        new_str+=str_number[-i]
    return int(new_str)

upper_bound=10**3
lower_bound=2

prime_dict={}

count=0
for i in range(lower_bound,upper_bound+1):
    if isPrime(i):
        print(i)
        count+=1
        prime_dict[i]=count

prime_list=list(prime_dict)
for i in range(len(prime_dict)):
    index=prime_dict[prime_list[i]] #21
    prime=prime_list[i] #73    
    
    if(digitMultiplication(prime)==index):
        mirror=getMirror(prime)
        
        index_mirror=getMirror(index)
        if prime_dict[mirror]==index_mirror:    
            print(prime," is the ",index,". prime number")
            print("its mirror is",mirror,"and mirror's index is",index_mirror)
    
