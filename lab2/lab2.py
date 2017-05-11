#Finding constants, variables and operators present in an expression

operators = ['+', '-', '*', '/', '%', '^']
expression = input("enter expression")
constants = []
variables = []
oper = []
for i in expression:
    if(i.isdigit()):
        constants.append(i)
    elif(i.isalpha()):
        variables.append(i)
    elif(i in operators):
        oper.append(i)
print("Constants : ", constants)
print("Variables : ", variables)
print("Operators : ", oper)

