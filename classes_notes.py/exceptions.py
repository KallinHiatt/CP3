#Ways to stop the errors from breaking
#try and except
#exceptions: ways that we handle errors created by users in a way that doesn't break the code.
#zero-division, file_not_found, value error, type error, index error
class NegativeNumberError(Exception):
    pass 


while True:
    try:
        numb = int(input("Tell me a number: "))
#TypeError? ValueError? What do they mean?
#if I was trying to subtract a string from a string, that would be a type error.
#converting to an integer would be valueerror
    except ValueError:
        print("You suck.")
    else: 
        break

while True:
    try:        
        num = int(input("Tell me another number: "))
        if num <= 0:
            raise NegativeNumberError("Cannot divide by negative number")
    except ValueError:
        print("You suck.")
    except NegativeNumberError as e:
        print(e)
    else:
        try:
            print(f"{str(numb)} divided by {str(num)} equals {numb / num} ")
            break
        except ZeroDivisionError:
            print("You can't divide by zero, try again.")
            continue
    finally:
        print("This code is over. Thanks for looking at it.")

