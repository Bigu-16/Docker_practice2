def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(str(num))



if __name__ == "__main__":
    print('Enter any number: ')
    number = int(input())
    
    fizzBuzz(number)