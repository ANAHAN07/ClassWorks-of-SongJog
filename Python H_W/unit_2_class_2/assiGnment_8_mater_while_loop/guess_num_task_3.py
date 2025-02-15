correct_num = 69
guess = None
while guess != correct_num:
    guess = int(input("Guess a number from the list 420, 88, 99, 69, 6969: "))   # Output: Guess a number from the list 420, 88, 99, 69, 6969: 77 / Guess a number from the list 420, 88, 99, 69, 6969: 69
    if guess != correct_num:
        print("Wrong, try again!")                                               # Output: Wrong, try again!
    else:
        print("Correct!")                                                       # Output: Correct!
