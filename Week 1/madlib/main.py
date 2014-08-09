noun = raw_input("Enter a noun ")
adjective = raw_input("Enter an adjective ")
verb = raw_input("Enter a verb ")
num1 = raw_input("Enter a number ")
num2 = raw_input("Enter another number ")
num3 = raw_input("Enter a smaller number than before ")
words = dict() #create dictionary object
words = {"Noun": noun, "Adjective": adjective, "Verb": verb}
numbers = [num1, num2, num3]

def calcQuo(a, b): #create function
    quo = int(a)/int(b) #turn parameters into integers so they can be divided
    return quo #return the quotient

per = calcQuo(num2, num3); #run function with variable parameters

i = 1
while i<=int(num2): #loop as many times as the value of num2
    print i
    i = i+1 #increase the value of the variable by one