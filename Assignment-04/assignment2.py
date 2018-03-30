def digitsget(num, digits = []):
    while num > 0:
        digits.append(num % 10)
        print(digits)
        return digitsget(num // 10, digits)
    if num == 0:
        return digits # return result


def multiply(digits, multiplier = 1):
    while len(digits) > 0:
        multiplier = multiplier * digits.pop(0)
        return multiply(digits, multiplier)
    if len(digits) == 0:
        return multiplier # return result


def persistence(num, count = 0):
    if num >= 10:
        num = multiply(digitsget(num)) # call method multiply
        count += 1
        return persistence(num, count) # call method persistence
    else:
        return count # return result

input_number = input("Enter integer number : ") # take the input number
number = int (input_number) # convert string to number
 
a = persistence(number) 
print(a) # call method by giving params