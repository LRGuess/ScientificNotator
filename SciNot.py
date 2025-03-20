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
    :return: A string representing the number in scientific notation.
    """
    #return "{:.3e}".format(number)
    format_string = "{:." + str(int(dec)) + "e}"
    return format_string.format(number)


num = float(input("Enter a number: "))
dec = float(input("Enter the number of significant digits: ")) - 1
print("Scientific notation:", to_scientific_notation(num, dec))