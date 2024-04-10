# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Run program: python3 run.py

import gspread
from google.oauth2.service_account import Credentials

# Import colorama for colored command line text (slightly below middle of page) https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python#:~:text=You%20can%20use%20the%20Colorama,for%20colored%20text%20in%20Python.
#  ANSI escape codes. and/with colorama python library
# I installed colorama with the following command (type in command line): - pip3 install colorama for Python 3 and pip install colorama for older versions of Python
from colorama import Fore

# Import python built-in module math used for basic math operations like: square root, exponents etc.
import math

# Import statistics Library used to calculate basic statistic like: arithmetic mean, median, spread, bell curce and interpolate
import statistics

# Import NumPy https://numpy.org/doc/stable/user/absolute_beginners.html
# import numpy as np

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('aircraft_data')


multirole_fighter = SHEET.worksheet('multirole_fighter')

data = multirole_fighter.get_all_values()

# print(data)

#------------------------------------------------------------------------------
def esc(code):
    """ Function somehow necessary for colorama
    """
    return f'\033[{code}m'

def get_airplane_data():
    """ Get and validate inputed airplane data. the input validation is made by
    calling a separate function validate_airplane_data()

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 10 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.

    Returns: airplane_data list (str and float) - incomplete user input data for one airplane.
    """

def validate_airplane_data():
    """
    Validates if user input is valid by checking data types(str and float), if there is exactly 10 values
    and that they are all positive and larger than zero.

    Inside the try, converts the fifth to tenth string values into integers.
    Raises ValueError if these strings cannot be converted into int and,
    or if there aren't exactly 10 values.

    Argumemts: airplane_data list (str and float) - incomplete user input data for one airplane.
    Returns: true or false
    """

def calc_wing_span():
    """ Calculates Wing span based on two values in the airplane_data list[].

    If statement selects which values to be used for calculation based on case 
    the user has choosen.

    Argumemts: incomplete airplane_data list (str and float) for one airplane.
               alternative stating wich case of dependancy variables should be used
    Returns: wing span
    """


def calc_aspect_ratio():
    """ Calculates Wing span based on two values in the airplane_data list[].

    If statement selects which values to be used for calculation based on case 
    the user has choosen.

    Argumemts: incomplete airplane_data list (str and float) for one airplane.
               alternative stating wich case of dependancy variables should be used
    Returns: wing span
    """


def calc_wing_area():
    """ Calculates Wing span based on two values in the airplane_data list[].

    If statement selects which values to be used for calculation based on case 
    the user has choosen.

    Argumemts: incomplete airplane_data list (str and float) for one airplane.
               alternative stating wich case of dependancy variables should be used
    Returns: wing span
    """


def calc_take_off_gross_weight():
    """ Calculates Wing span based on two values in the airplane_data list[].

    If statement selects which values to be used for calculation based on case 
    the user has choosen.

    Argumemts: incomplete airplane_data list (str and float) for one airplane.
               alternative stating wich case of dependancy variables should be used
    Returns: wing span
    """


def calc_wing_loading():
    """ Calculates Wing span based on two values in the airplane_data list[].

    If statement selects which values to be used for calculation based on case 
    the user has choosen.

    Argumemts: incomplete airplane_data list (str and float) for one airplane.
               alternative stating wich case of dependancy variables should be used
    Returns: wing span
    """


def feedback_on_airplane_data():
    """
    Review airplane data and give feedback to the user if any of the user provided airplane data 
    Appear to be extreme.

    Argumemts: complete airplane_data list (str and float) for one airplane.
    """


def uppdate_dependent_airplane_data():
#------------------------------------------------------------------------------
    """ Fills in the blank values in the user provided airplane_data-list
    by function calls to separate functions that calculates these values.

    These values has been intentionaly left blank by the user as instructed 
    by the function xxxxxxxxxxx. The reason for leaving some values blank
    is that values are interdependent. Inputting all values would therfore
    over-define (overdetermine) the airplane-data.

    Argumemts: airplane_data list (str and float) - incomplete user input data for one airplane.
    Returns: airplane_data list (str and float) - completed user input data for one airplane.
    """


def push_airplane_data_to_worksheet():
    """ Update the relevant worksheet with the data provided
    """


def select_and_pull_airplane_data_from_worksheet():
    """
    selecs and collects columns of airplane data from worksheet,
    and returns the data as a list of lists.
    """


def Input_case():
    """ x
    """

def calc_mean():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://www.w3schools.com/python/ref_stat_mean.asp
    https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """
    # print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
    # numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)[source]


def calc_median():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://www.w3schools.com/python/ref_stat_median.asp#:~:text=median()%20method%20calculates%20the,in%20a%20set%20of%20data.
    https://numpy.org/doc/stable/reference/generated/numpy.median.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """
    # print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
    # numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)[source]


def calc_variance():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://www.w3schools.com/python/ref_stat_variance.asp
    https://numpy.org/doc/stable/reference/generated/numpy.var.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """
    # print(statistics.variance([1, 3, 5, 7, 9, 11]))
    # numpy.var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)


def create_meta_data_table():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    Argumemts: airplane_data_select_parameter[]
    Returns: 
    """


def calc_bell_curve():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """
    # numpy.random.normal(loc=0.0, scale=1.0, size=None)


def calc_inbetween_point():
    """ Calculate (interpolate and extrapolate) value for a  for a value in airplane_data[].

    https://numpy.org/doc/stable/reference/generated/numpy.interp.html

    Argumemts: x
    Returns: mean wing span value
    """
    # numpy.interp(x, xp, fp, left=None, right=None, period=None)[source]

def main():

    """ Run all program functions
    
        Parameters:
        Requests user to input a number between 1-5
        If statement executes a function dependent on input
        1: place_order()
        2: view_live_orders()
        3: exits system using sys.exit()
        Else requests the user tries again

    Argumemts:
    Returns:
    """





# Welcome message
print("\033[1;34;40mx x x x      x      x x x x   x x x x   x x x x   x x x x   x         x x x x   x x x x")
print("x           x x     x     x   x     x   x         x     x   x         x     x      x")
print("x x x x    x   x    x x x x   x x x x   x x x x   x x x x   x         x     x      x")
print("      x   x x x x   x         x         x         x   x     x         x     x      x")
print("x x x x  x       x  x         x         x x x x   x     x   x x x x   x x x x      x\n")
print(Fore.WHITE +"                                                                       Copyright: Gustaf Enebog 2024")
print("Welcome to SAPPERLOT - Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool\n")
print("Do you want to read the instructions? y/n\n")


# Main Menu
# print("1. Add data 2. Edit data 3. Delete data 4. Meta data 5. Inbetween points 6. HELP")
print("Please select an option by entering a number between 1-6:")
print("1. Add data")
print("2. Edit data")
print("3. Delete data")
print("4. Meta data")
print("5. Inbetween points")
print("6. HELP")
