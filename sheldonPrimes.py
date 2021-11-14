#checks if a number is prime
def isPrime(number): 
    if number<=1:
        return 0  #number is not a prime number
    else:
        for i in range(2,number):
            if number%i==0:
                return 0 #number is not a prime number
        return 1 #number is prime number

#checks if number's digits product equals to number's order in prime numbers
def productProperty(number,order): 
    digit_product=1 #holds result of digit product 
    while number!=0: 
        digit_product=digit_product*(number%10) #multiplies the digit product with units digit
        number=number//10 #updates the number with deleting the units digit
    if digit_product==order: #if result equals number's order 
        return 1
    else:
        return 0
    
#reverse the number last digit to first digit
def reverseNumber(number): 
    string_number=str(number) #converts the number to string 
    new_string="" # will hold the reversed number in string type
    
    for i in range(1,len(string_number)+1): # i's range is 1 to length+1 since we will use the index with  minus sign
        new_string += string_number[-i] #adds number's digits to new_string from end of the number
    
    reversed_number=int(new_string) #converts the reversed number from string to integer type
    return reversed_number #returns reversed number


#fills the prime list with prime numbers and orders
def fillPrimeList(upper_bound):
    prime_list=[] #holds prime numbers and orders
    order=0
    for number in range(upper_bound): #loop turns numbers 0 to upper_bound
        if isPrime(number): #checks if each number is prime 
            order+=1
            prime_list.append([number,order]) #add prime numbers to prime_list
    return prime_list

#prints the prime number if it provides the mirror property
def mirrorProperty(prime_list):
    for i in range(len(prime_list)): # checks each prime number in prime_list
        prime_number=prime_list[i][0] #the prime number
        order=prime_list[i][1] #prime number's order
        if productProperty(prime_number, order): #if the prime number supplies product property
            mirror_prime=reverseNumber(prime_number) #take the prime numbers reverse
            mirror_order=reverseNumber(order) #take the prime number's order's reverse

            if(prime_list[mirror_order-1][0]==mirror_prime): # if reverse prime number's order equals the reverse order print the data 
                print("The prime number",prime_number,"'s order is",order) 
                print("Its reverse",mirror_prime,"'s order is",mirror_order)
                print("---------------------------------------")
                print(prime_number,"is a perfect prime number")                    
                
upper_bound=10**4 #define upper bound
prime_list=fillPrimeList(upper_bound)
mirrorProperty(prime_list)
