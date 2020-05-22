def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print('Why do we use functions?')
    
    print('1. It allows us to use the same piece of code more than once.')
    print('2. Functions make our code more readable to others.')
    print('3. Some functions are built into python with handy algorithms.')
    print('4. All of the above.')

    while int(input()) != 4:
        print('Please, try again.')
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Soraya', '2020')
remind_name()
guess_age()
count()
test()
end()
