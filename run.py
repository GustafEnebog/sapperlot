# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Run program: python3 run.py

import gspread
from google.oauth2.service_account import Credentials

#Import OS Library
import os

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

def main_menu_select():
    """ Handles selection from main menu
    """
    print('MAIN MENU')
    print('1. Add data')
    print('2. Edit data')
    print('3. Delete data')
    print('4. Meta data')
    print('5. Bell curve')
    print('6. Inbetween points')
    print('7. HELP')
    print('8. QUIT PROGRAM\n')

    while True:
        selection_main_menu = input('\nPlease select an option by entering a number between 1-6:\n')
        if selection_main_menu == '1':
            get_airplane_data()
            
        elif selection_main_menu == '2':
            edit_data()
            
        elif selection_main_menu == '3':
            delete_data()
            
        elif selection_main_menu == '4':
            create_meta_data_table()
            
        elif selection_main_menu == '5':
            create_bell_curve_graph()

        elif selection_main_menu == '6':
            calc_inbetween_outside_point()

        elif selection_main_menu == '7':
            help()

        #Abort the current running process
        elif selection_main_menu == '8':
            os.abort()

        else:
            print('Invalid choice, please enter a number between 1-6,\n')
            continue


def get_airplane_data():
    """ Get and validate inputed airplane data. the input validation is made by
    calling a separate function validate_airplane_data()

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 10 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.

    Returns: airplane_data list (str and float) - incomplete user input data for one airplane.
    """


    # Sub menu - Add data
    print('In the next step you will be asked to enter three out of the\nfollowing five aircraft parameters:\nWing span, Aspect ratio, Wing area, Max takeoff weight, Wing loading.\n')
    print('This is to not over-define the data. The program will calculate these values for you!')

    print('1. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('2. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, Max takeoff weight, '  + esc('238;2;9') + 'Wing loading' + esc(0))
    print('3. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('4. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, Max takeoff weight, ' + esc('238;2;9') + 'Wing loading'  + esc(0))
    print('5. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight, Wing loading')
    print('6. Wing span, ' + esc('238;2;9') + 'Aspect ratio,'  + esc(0) + ' ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight'  + esc(0) + ', Wing loading')
    print('7. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('8. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,' + esc(0) + ' Max takeoff weight, ' + esc('238;2;9') + 'Wing loading\n'  + esc(0))
    print('Or type 0 to return to main menu\n')
    input('Please select an option by entering a number between 0-8:\n')


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


def edit_data():
    """ Edit the relevant worksheet with the data provided
    """
    print('Please select an option by entering a number between 0-x:')


def delete_data():
    """ Edit the relevant worksheet with the data provided
    """
    print('Please select an option by entering a number between 0-x:')


def push_airplane_data_to_worksheet():
    """ Update the relevant worksheet with the data provided
    """


def select_and_pull_airplane_data_from_worksheet():
    """
    selecs and collects columns of airplane data from worksheet,
    and returns the data as a list of lists.
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

    print("Meta data - Please select an option by entering a number between 0-x:")


def create_bell_curve_graph():
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


def calc_inbetween_outside_point():
    """ Calculate (interpolate and extrapolate) value for a  for a value in airplane_data[].

    https://numpy.org/doc/stable/reference/generated/numpy.interp.html

    Argumemts: x
    Returns: mean wing span value
    """
    # numpy.interp(x, xp, fp, left=None, right=None, period=None)[source]
    # Note - The datas independent variable needs to be sorted so that it is increasing!

    print("Please choose an airplane parameter whose value you want to evaluate/estimaten\nbetween (interpolate) or outside (extrapolate) of it's data points")
    print('1. Wing span')
    print('2. Aspect ratio')
    print('3. Wing area')
    print('4. Max takeoff weight')
    print('5. Wing loading')
    input('Please select an option by entering a number between 0-x:')
    print('Note in the case of extrapolation that the reliability of estimate\nquickly deteriate for estimates as estimates moves away from the data points')
    input('Please choose a second airplane parameter you want to use as the independent vaiable\n(you have just given the dependent parameter) for the interpolation')


def help():

    """ Display help text

    Argumemts:
    Returns:
    """
    input('Do you want to read the instructions? y/n\n')
    print('HELP text here')


def main():
    """ Run all program functions

    Argumemts:
    Returns:
    """
    main_menu_select()


# Welcome message
print('\033[1;34;40mx x x x      x      x x x x   x x x x   x x x x   x x x x   x         x x x x   x x x x')
print('x           x x     x     x   x     x   x         x     x   x         x     x      x')
print('x x x x    x   x    x x x x   x x x x   x x x x   x x x x   x         x     x      x')
print('      x   x x x x   x         x         x         x   x     x         x     x      x')
print('x x x x  x       x  x         x         x x x x   x     x   x x x x   x x x x      x\n')
print(Fore.WHITE +'                                                                       Copyright: Gustaf Enebog 2024')
print('Welcome to SAPPERLOT - Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool\n')


main()