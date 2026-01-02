"""Write_function"""

def is_leap(year: int):
    """calculate a leap year
    input: 
    year: year to calculate

    """
    leap = False
    if year % 4 == 0:
        leap = True if year % 100 != 0 else False or True if year % 400 == 0 else False
    return leap

print(is_leap(int(input())))
