#Conversion of Non-deterministic Finite Automata (NFA) to Deterministic Finite Automata (DFA)

dfa_expression = {}
#nfa_expression = {'a': {'1': ['0'], '0': ['b']}, 'b': {'1': ['b', 'c'], '0': ['0']}, 'c': {'1': ['c'], '0': ['0']},}
nfa_expression = {}

def create_transition_table_for_NFA():
    y = 'y'
    while y=='y':
        variable = input("Enter state : ")
        domains = input("Enter inputs of %c : "%variable)
        list_domains = domains.split(',')
        if variable not in nfa_expression:
            nfa_expression[variable] = {i:[] for i in list_domains}
            print (nfa_expression)
            for i in list_domains:
                next_state = input("Enter next state of %c when domain is %c : "%(variable,i))
                list_nextstate = next_state.split(',')
                for j in list_nextstate:
                    nfa_expression[variable][i].append(j)
        y = input("Continue?y/n : ")

create_transition_table_for_NFA()

start_state = input("Enter start state : ")
queue = [[start_state]] #keeps track of all the variable and pops using FIFO technique
visited = []

def store_next_state(i):
    s = ''
    temp_dict = {'0': [], '1': []}
    for j in temp_dict.keys():
        if len(nfa_expression[i][j]) == 1:
            temp_dict[j] = nfa_expression[i][j]
        else:
            for k in nfa_expression[i][j]:
                s = s + k
            temp_dict[j] = [s]
    return temp_dict

def update_final_dict(final_dict, temp_dict):
    for i in temp_dict.keys():
        temp = temp_dict[i] #List
        for j in temp:
            final_dict[i].append(j)
    return final_dict

def _get(var):
    final_dict = {'0': [], '1':[]}
    for i in var:
        temp_dict = store_next_state(i)
        final_dict = update_final_dict(final_dict, temp_dict)

    for i in final_dict.keys():
        s = ''
        _ = final_dict[i]
        for j in _:
            s = s + j
        temp = set(s)
        s = ''
        for j in temp:
            s = s + j
        final_dict[i] = [s]

    return final_dict

def should_pass(visited, queue):
    count = 0
    l = len(queue)
    for i in queue:
        if i in visited:
            count += 1
    if count == l:
        return False
    else:
        return True

def convert():
    next_state = {}
    while True:
        #get the present state
        present_state = queue.pop(0)
        var = present_state[0]
        visited.append([var])
        #call function to store the next state values of the present state in next_state
        #next_state = store_next_state(var) #Dictionary type
        next_state = _get(var)
        #update queue
        for j in next_state.keys():
            if next_state[j] != ['0']:
                queue.append(next_state[j])
        #call function to update DFA
        dfa_expression[var] = next_state

        if not should_pass(visited, queue):
            break
    print ("dfa final : ", dfa_expression)

convert()