def sum(a, b):
	return a + b
def minus(a, b):
	return a - b
def multi(a, b):
	return a * b
def divis(a, b):
	return a / b
def choose():
	print ('Choose:')
	print ('"+" "-" "*" "/"')
	action = input

print ('Enter first number')
first_number = input()
print ('Choose:')
print ('"+" "-" "*" "/"')
action = input()
print ('Enter second number')
second_number = input() 

match calcul():
    case action == '+':
         first_number + second_number
    case action == '-':
         afirst_number - second_number
    case action == '*':
         first_number * second_number
    case action == '/':
         first_number / second_number        
    case _:
        action-default

calcul(action, first_number, second_number)        