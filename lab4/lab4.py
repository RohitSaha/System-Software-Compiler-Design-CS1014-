#Regular Expression (RE) to Non-Deterministic Finite Automata (NFA)

'''
This function is used to detect how many states are required to process the string.
States are in the form of characters. This function will place the characters a.k.a states in the
correct position of the regular expression and return the newly formed string.
'''
def normalize(reg_ex):
    val = 97
    in_bracket = False
    inp = ['0', '1']
    operator = ['+', '-', '/', '*', ')']
    l = len(reg_ex)
    for i in range(l+100):
        try:
            if reg_ex[i] == '(':
                in_bracket = True
            if reg_ex[i] == ')':
                in_bracket = False

            if reg_ex[i] in inp:
                #current pointer is digit
                #print reg_ex[i]
                if reg_ex[i+1] in inp or reg_ex[i+1] == '(':
                    #print reg_ex[i],reg_ex[i+1], "in"
                    if in_bracket == False:
                      #if followed by another digit
                        reg_ex = reg_ex[0:i+1] + chr(val) + reg_ex[i+1:]
                        val += 1
                elif reg_ex[i+1] in operator:
                    #if followed by an operator
                    pass

                #print reg_ex


            if reg_ex[i] in operator:
                #current pointer is an operator
                if reg_ex[i+1] in inp:
                    #if followed by a digit
                    if in_bracket == False:
                        reg_ex = reg_ex[0:i+1] + chr(val) + reg_ex[i+1:]
                        val += 1
                        i += 1
                elif reg_ex[i+1] in operator:
                    #if followed by another operator
                    pass
        except:
            print ("Pass")
            break

    reg_ex += chr(val)
    return reg_ex


'''
This function is used to initiate a dictionary based on the normalized string.
Normalized string contains the states in the form of characters and inputs that are possible for every state.
This funciton will create a dictionary with keys as states and values as {'0':[], '1':[]}.
'''
def initiate_dict(norm_exp):
    variables = []
    digits = []
    state = {}

    #Count alphas and digits. Alphas = states, digits = inputs
    for i in norm_exp:
        if i.isalpha():
            variables.append(i)
        elif i.isdigit():
            digits.append(i)
    digits = set(digits)

    for i in variables:
        state[i] = {j:[] for j in digits}

    return state


'''
Based on the contents in pre_exp and post_exp, the state dictionary will be updated.
Every state's next state will be updated.
'''
def update_dict(pre_exp, post_exp, i, get_dict):
    digits = []
    #Checking pre-expression of 'i'
    if '*' in pre_exp:
        #Now check for the inputs in this string
        for exp in pre_exp:
            if exp.isdigit():
                digits.append(exp)
        digits = set(digits)
        for digit in digits:
            get_dict[i][digit].append(i)
    digits = []
    for exp in post_exp:
        if exp.isdigit():
            digits.append(exp)
    digits = set(digits)
    for digit in digits:
        get_dict[i][digit].append(chr(ord(i) + 1))
    return get_dict

def get_inputs(norm_exp, get_dict):
    count = 0
    post_exp = ''
    for i in range(len(norm_exp)):
        if norm_exp[i].isalpha():
            if count == 0:
                pre_exp = norm_exp[0:i]
                count += 1
            else:
                pre_exp = post_exp
            post_exp = ''
            for j in range(i+1, len(norm_exp)):
                if norm_exp[j].isalpha() == False:
                    post_exp += norm_exp[j]
                else:
                    break
            get_dict = update_dict(pre_exp, post_exp, norm_exp[i], get_dict)
    return get_dict

def main():
    reg_ex = input("Enter regular expression : ")
    norm_exp = normalize(reg_ex)
    print (norm_exp)
    get_dict = initiate_dict(norm_exp)

    get_final = get_inputs(norm_exp, get_dict)
    print ("NFA : ", get_final)

#(0+1)*01
main()