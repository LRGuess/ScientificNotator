#============================================
#   Written by Liam Ramirez-Guess
#   Created on March 20th, 2025
#   Tested on CASIO calculators
#   Licenced under GNU General Public License v3.0   
#============================================

def to_scientific_notation(number, dec):
    """
    Converts a number into scientific notation.
    :param number: The number to convert.
    :param dec: The number of significant digits.
    :return: A string representing the number in scientific notation.
    """
    #return "{:.3e}".format(number)
    format_string = "{:." + str(int(dec)) + "e}"
    return format_string.format(number)


try:
    num = float(input("Number: "))
    dec = float(input("Sig Digs: ")) - 1
    print("Sci Not:", to_scientific_notation(num, dec))
except ValueError:
    print("Enter numeric values!")
