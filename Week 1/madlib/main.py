'''
Justin Henry
DWP - Online
8/8/2014
'''

#Prompts for user to enter strings and numbers
noun = raw_input("Enter a noun ")
adjective = raw_input("Enter an adjective ")
verb = raw_input("Enter a verb ")
num1 = raw_input("Enter a number ")
num2 = raw_input("Enter another number ")
num3 = raw_input("Enter a smaller number than before ")

#Objects to contain strings and numbers
words = dict()
words = {"Noun": noun, "Adjective": adjective, "Verb": verb}
numbers = [num1, num2, num3]

#Function for determining a quotient
def calcQuo(a, b):
    quo = int(a)/int(b) #turn parameters into integers so they can be divided
    return quo
per = calcQuo(num2, num3); #run function with variable parameters

#Conditional to change article
article =""
if noun.startswith('a') or noun.startswith('e') or noun.startswith('i') or noun.startswith('o') or noun.startswith('u'):
    article = "an"
else:
    article = "a"

#The madlib string
print "There was once " + article + " " + noun + " with quite the " + adjective + " face. It tried to " + verb + " " + str(num1) + " times but was unsuccessful. It assumed, however, that if it tried " + str(num2) + " more times, it would finally succeed. With only " + str(num3) + " days left, it had better hurry and get to work. It has got to try to " + verb + " " + str(per) + " times each of the next " + str(num3) + " days to accomplish its goal. Let's watch it work!"

#A loop to run as many times as the value of num2
i = 1
while i<=int(num2):
    print str(i) + " and a..."
    i = i+1
    if i > int(num2): #When the loop reaches the value of num2
        print "SUCCESS!"

