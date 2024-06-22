import random
#to choose a random number
def slect_randm_num(minn, maxx):
    rnd = random.randint(minn, maxx)
    return rnd
#the guessin' part
def guessing(guess, minn, maxx):
    print("I selected a number! try and guess it! \ndw I will give you hints to help with guessing the number ")
    status = True
    counter = 0
    while status == True:
        plyr_guess = input()
        try:
            plyr_guess = int(plyr_guess)
        except:
            print("Please Enter a valid input..tsk tsk")
            break
        if (plyr_guess >= minn and plyr_guess <= maxx) == False:
            print("Ayo.. off range.. try again")
            continue
        while plyr_guess >= minn and plyr_guess <= maxx:
            if plyr_guess == guess:
                print("YOU GOT IT")
                status = False
                break
            elif plyr_guess > guess:
                print("BRO,you set the bar a little too high.. try again")
                break
            else:
                print("The number you choose is smaller than what I want... try again")
                break
        counter += 1
    print("you did guess", counter, "times!")
#greeting 'cause why not
def greet():
    print("Hola.. Mi nombre es DORA.. Dora the explorer!")
    print("just kidding.. I am guessie (my maker was lazy asf I know)")
    print("I am your new guessing numbers game")
    print(" ")
    print("Here's the rules: gimme a range and I will choose a number and your job is to guess it .. duh ez enough")
    print("Ready.. let's go!")

#setting the range
def range():
    print("Ayo gimme a range")
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            print("Invalid range.. bye")
            exit()
        if num1 != num2:
            if num1 > num2:
                maxxie = num1
                minnie = num2
                break
            else:
                maxxie = num2
                minnie = num1
                break
    return minnie, maxxie


greet()
(mi_n, ma_x) = range()
guessing(slect_randm_num(mi_n, ma_x), mi_n, ma_x)