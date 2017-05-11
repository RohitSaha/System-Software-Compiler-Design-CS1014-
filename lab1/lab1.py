#File operations

def enter_word():
    word = input("Enter word to be appended")
    f = open('lab1file.txt', mode='a')
    f.write(word)
    f.close()

def replace_word():
    search_word = input("Enter word to be replaced")
    l = len(search_word)
    f = open('lab1file.txt', mode='r').read()
    for i in range(0, len(f)-1):
        if(search_word == f[i:i+l]):
            new_word = input("Enter word to be inserted")
            f = f[0:i] + new_word + f[i+l:]
            break
    g = open('lab1file.txt', mode='w')
    g.write(f)
    g.close()

def print_contents():
    f = open('lab1file.txt', mode='r').read()
    print("Contents of the file : \n")
    print(f)

def control():
    y = 'y'
    while(y == 'y'):
        print("1. Append word  2. Replace word  3. Print")
        option = int(input("Enter choice"))
        if option==1:
            enter_word()
        elif option == 2:
            replace_word()
        elif option == 3:
            print_contents()
        y = input("continue?y/n")

control()




