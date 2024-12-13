"""
This function adds every value in a list together and returns it
"""
def add(values:list[float]):
    total = 0
    for n in values:
        total += n
    return total
"""
Subtracts every value in a list from the first and returns it
"""
def subtract(values:list[float]):
    total = values[0]
    for n in values[1:]:
        total -= n
    return total

"""
Multiply every non-zero value in a list together and return it
"""
def multiply(values:list[float]):
    total = 0
    for n in values:
        if n != 0:
            if total == 0:
                total = n
            else:
                total *= n
    return total

"""
Divides the first number by every following number and returns it,
throws ZeroDivisionError if zero any number other than the starting value
"""
def divide(values:list[float]):
    total = values[0]
    for n in values[1:]:
        if n != 0:
            total /= n
        else:
            raise ZeroDivisionError
    return total