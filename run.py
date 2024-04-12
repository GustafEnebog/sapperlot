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
    print('6. Inbetween points     "H" HELP     "Q" QUIT PROGRAM')

    while True:
        selection_main_menu = input('\nPlease select an option by entering a number between 1-6 an H or Q:\n')
        if selection_main_menu == '1':
            unconverted_airplane_data = get_airplane_data()
            converted_airplane_data = convert_to_int(unconverted_airplane_data)
            airplane_data = uppdate_dependent_airplane_data(converted_airplane_data)
            push_airplane_data_to_worksheet(airplane_data)  # loveSandwiches code also have a worksheet as an argument. I took it away since it does not work since it is not defined
            break
        elif selection_main_menu == '2':
            edit_data()
            break
        elif selection_main_menu == '3':
            delete_data()
            break
        elif selection_main_menu == '4':
            create_meta_data_table()
            break
        elif selection_main_menu == '5':
            create_bell_curve_graph()
            break
        elif selection_main_menu == '6':
            calc_inbetween_outside_point()
            break
        elif selection_main_menu == 'H':
            help()
            break
        elif selection_main_menu == 'Q':
            os.abort()  #Abort the current running process
        else:
            print('Invalid choice, please enter a number between 1-6 an H or Q:\n')
            continue


def get_airplane_data():
    """ Get and validate inputed airplane data. the input validation is made by
    calling a separate function validate_airplane_data()

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 10 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.

    Based on "get_sales_data()" in loveSandwiches, AJGreaves at Code Institute https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1

    Returns: airplane_data list (str and float) - incomplete user input data for one airplane.
    """

    # Sub menu - FIRST choise
    print('\nIn the next step you will be asked to enter three out of the\nfollowing five aircraft parameters:\nWing span, Aspect ratio, Wing area, Max takeoff weight, Wing loading.')
    print('This is to not over-define the data. The program will calculate these values for you!')
    print('\n1. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('2. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, Max takeoff weight, '  + esc('238;2;9') + 'Wing loading' + esc(0))
    print('3. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('4. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, Max takeoff weight, ' + esc('238;2;9') + 'Wing loading'  + esc(0))
    print('5. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight, Wing loading')
    print('6. Wing span, ' + esc('238;2;9') + 'Aspect ratio,'  + esc(0) + ' ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight'  + esc(0) + ', Wing loading')
    print('7. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('8. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,' + esc(0) + ' Max takeoff weight, ' + esc('238;2;9') + 'Wing loading'  + esc(0))
    print('"H" HELP          "M" BACK TO MAIN MENU          "Q" QUIT PROGRAM')

    global selection_sub_menu_dep_variable
    while True:
        selection_sub_menu_dep_variable = input('\nPlease select an alternative by entering a number between 1-8 an H, M or Q:\n')
        if selection_sub_menu_dep_variable == '1':
            print('\nYou selected to leave out "Wing span" and "Max Takeoff Weight" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio, wing_area, 0, wing_loading (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '2':
            print('\nYou selected to leave out "Wing span" and "Wing loading" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio, wing_area, max_takeoff_weight, 0 (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '3':
            print('\nYou selected to leave out "Aspect Ratio" and "Max Takeoff Weight" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, wing_span, 0, wing_area, 0, wing_loading (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '4':
            print('\nYou selected to leave out "Aspect Ratio" and "Wing loading" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, wing_span, 0, wing_area, max_takeoff_weight, 0 (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '5':
            print('\nYou selected to leave out "Wing span" and "Wing Area" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio, 0, max_takeoff_weight, wing_loading (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '6':
            print('\nYou selected to leave out "Aspect Ratio" and "Wing Area" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, wing_span, 0, 0, max_takeoff_weight, wing_loading (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '7':
            print('\nYou selected to leave out "Wing Area" and "Max Takeoff Weight" (replace value with 0). Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, wing_span, aspect_ratio, 0, 0, wing_loading (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == '8':
            print('\nYou selected to leave out "Wing Area" and "Wing loading". Your data to be entered should therefore have this format:\nairplane_name, manufacturer, country, category, year, wing_span, aspect_ratio, 0, max_takeoff_weight, 0 (so 10 items including the two zero)\n')
            break
        elif selection_sub_menu_dep_variable == 'H':
            help()
            break  # Should this break be here or is not necessary since it goes to this function anyway!?
        elif selection_sub_menu_dep_variable == 'M':
            main_menu_select()
            break  # Should this break be here or is not necessary since it goes to this function anyway!?
        elif selection_sub_menu_dep_variable == 'Q':
            os.abort()  #Abort the current running process
        else:
            print('Invalid choice, please enter a number between 1-8 an H, M or Q:\n')
            continue

    # Sub menu - SECOND choise
    while True:
        inputted_airplane_data_str = input("Please enter the data here:\n")
        inputted_airplane_data = inputted_airplane_data_str.split(",")
        if validate_airplane_data(inputted_airplane_data):
            print("Data is valid!")
            break

    return inputted_airplane_data


def validate_airplane_data(values):
    """
    Validates if user input is valid by checking data types(str and float), if there is exactly 10 values
    and that they are all positive and larger than zero.

    Inside the try, converts the fifth to tenth string values into integers.
    Raises ValueError if these strings cannot be converted into int and,
    or if there aren't exactly 10 values.

    Based on "validate_data()" in loveSandwiches, AJGreaves at Code Institute https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1

    Argumemts: airplane_data list (str and float) - incomplete user input data for one airplane.
    Returns: true or false
    """
    try:
        if len(values) != 10:  # 10 items in a list starting at index 0 running untill index 9
            print(values)
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
        # [int(value) for value in values]
        for i in range(4, 9):  # 10 items in a list starting at index 0 running untill index 9
            int(values[i])
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def convert_to_int(unconverted_airplane_data):
    """ Converts the numeric data (year, wing_span, aspect_ratio, wing_area, max_takeoff_weight, wing_loading) to integers

    Argumemts: 
    Returns: 
    """
    converted_airplane_data = unconverted_airplane_data  # Looks not so right but it makes it work!
    for i in range(4, 9):
        converted_airplane_data[i] = int(unconverted_airplane_data[i])
    return converted_airplane_data


def feedback_on_airplane_data():
    """
    Review airplane data and give feedback to the user if any of the user provided airplane data 
    Appear to be extreme.

    Argumemts: complete airplane_data list (str and float) for one airplane.
    """

def uppdate_dependent_airplane_data(converted_airplane_data):
    """ Fills in the blank values in the user provided airplane_data-list
    by function calls to separate functions that calculates these values.

    These values has been intentionaly left blank by the user as instructed 
    by the function xxxxxxxxxxx. The reason for leaving some values blank
    is that values are interdependent. Inputting all values would therfore
    over-define (overdetermine) the airplane-data.

    https://docs.google.com/spreadsheets/d/186F_QSx24xYlkzunnzrzawt06MJO8GfdPsxGeRoqIa4/edit#gid=1680754323

    Based on "update_worksheet()" in loveSandwiches, AJGreaves at Code Institute https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1

    Argumemts: airplane_data list (str and float) - incomplete user input data for one airplane.
    Returns: airplane_data list (str and float) - completed user input data for one airplane.
    """
    airplane_data = converted_airplane_data
    if selection_sub_menu_dep_variable == '1':
        airplane_data[5] = math.sqrt(converted_airplane_data[6] * converted_airplane_data[7])
        airplane_data[8] = converted_airplane_data[9] * converted_airplane_data[7]
    elif selection_sub_menu_dep_variable == '2':
        airplane_data[5] = math.sqrt(converted_airplane_data[6] * converted_airplane_data[7])
        airplane_data[9] = converted_airplane_data[8] / converted_airplane_data[7]
    elif selection_sub_menu_dep_variable == '3':
        airplane_data[6] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[7]
        airplane_data[8] = converted_airplane_data[9] * converted_airplane_data[7]
    elif selection_sub_menu_dep_variable == '4':
        airplane_data[6] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[7]
        airplane_data[9] = converted_airplane_data[8] / converted_airplane_data[7]
    elif selection_sub_menu_dep_variable == '5':
        airplane_data[5] = math.sqrt(converted_airplane_data[6] * (converted_airplane_data[8] / converted_airplane_data[9]))  # Special case equation 1
        airplane_data[7] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[6]
    elif selection_sub_menu_dep_variable == '6':
        airplane_data[6] = math.pow(converted_airplane_data[5],2) / (converted_airplane_data[8] / converted_airplane_data[9])  # Special case equation 2
        airplane_data[7] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[6]
    elif selection_sub_menu_dep_variable == '7':
        airplane_data[7] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[6]  # Special case equation 3
        airplane_data[8] = converted_airplane_data[9] * (converted_airplane_data[8] / converted_airplane_data[9])  # Special case equation 4
    elif selection_sub_menu_dep_variable == '8':
        airplane_data[7] = math.pow(converted_airplane_data[5],2) / converted_airplane_data[6]  # Special case equation 3
        airplane_data[9] = converted_airplane_data[8] / (converted_airplane_data[8] / converted_airplane_data[9])  # Special case equation 5
    elif selection_sub_menu_dep_variable == 'H':
        help()
    elif selection_sub_menu_dep_variable == 'M':
        main_menu_select()
    elif selection_sub_menu_dep_variable == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-8 an H, M or Q:\n')

    print(airplane_data)

    return airplane_data


def edit_data():
    """ Edit the relevant worksheet with the data provided
    """
    print('Please select an option by entering a number between 0-x:')


def delete_data():
    """ Edit the relevant worksheet with the data provided
    """
    print('Please select an option by entering a number between 0-x:')


def push_airplane_data_to_worksheet(data):  # loveSandwiches code also have a worksheet as an argument. I took it away since it does not work since it is not defined
    """ Update the correct tab in worksheet with data in the form of
    a list of string and integer values
    """
    # print(f"Updating {worksheet} worksheet...\n")
    if data[3] == 'multirole_fighter':
        worksheet_to_update = SHEET.worksheet('multirole_fighter')
        worksheet_to_update.append_row(data)
        print('The "multirole_fighter"-category/tab in our worksheet updated successfully\n')
        # print(f"{'multirole_fighter'} worksheet updated successfully\n")
    elif data[3] == 'airliner':
        worksheet_to_update = SHEET.worksheet('airliner')
        worksheet_to_update.append_row(data)
        print('The "airliner"-category/tab in our worksheet updated successfully\n')
    elif data[3] == 'general_aviation':
        worksheet_to_update = SHEET.worksheet('general_aviation')
        worksheet_to_update.append_row(data)
        print('The "general_aviation"-category/tab in our worksheet updated successfully\n')
    else:
        print('Ouuups, you must have misspelled the fourth entry (category). It should be Multirole Fighter, Airliner or General Aviation. sorry, but this error really should have been caught earlier!')

    # multirole_fighter = SHEET.worksheet('multirole_fighter')  ???????? Where have I gotten these from? Can I throw them away??????????
    # data = multirole_fighter.get_all_values()  ???????? Where have I gotten these from? Can I throw them away??????????

    # print(f"Updating {worksheet} worksheet...\n")
    # worksheet_to_update = SHEET.worksheet(worksheet)
    # worksheet_to_update.append_row(data)
    # print(f"{worksheet} worksheet updated successfully\n")


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
    input('Please select an option by entering a number between 0-x:\n')
    print('Note in the case of extrapolation that the reliability of estimate\nquickly deteriate for estimates as estimates moves away from the data points')
    input('Please choose a second airplane parameter you want to use as the independent vaiable\n(you have just given the dependent parameter) for the interpolation\n')


def help():

    """ Display help text

    Argumemts:
    Returns:
    """
    input('Do you want to read the instructions? y/n\n')
    print('HELP text here')


def main():
    """ Run all program functions
    
    Lifecycle of the user input alternative nr 1 from the main menu:
    inputted_airplane_data -> unconverted_airplane_data -> converted_airplane_data -> airplane_data

    Argumemts:
    Returns:
    """
    main_menu_select()
    # print('BEFORE get_airplane_data')
    # unconverted_airplane_data = get_airplane_data()
    # print('AFTER get_airplane_data')
    # converted_airplane_data = convert_to_int(unconverted_airplane_data)
    # THIS = print(converted_airplane_data)
    # airplane_data = uppdate_dependent_airplane_data(converted_airplane_data)
    # there_should_not_be_any_holes_now = print(airplane_data)

    # data = get_airplane_data()
    # sales_data = [int(num) for num in data]
    # update_worksheet(sales_data, "sales")


# Welcome message
print('\033[1;34;40mx x x x      x      x x x x   x x x x   x x x x   x x x x   x         x x x x   x x x x')
print('x           x x     x     x   x     x   x         x     x   x         x     x      x')
print('x x x x    x   x    x x x x   x x x x   x x x x   x x x x   x         x     x      x')
print('      x   x x x x   x         x         x         x   x     x         x     x      x')
print('x x x x  x       x  x         x         x x x x   x     x   x x x x   x x x x      x\n')
print(Fore.WHITE +'                                                                       Copyright: Gustaf Enebog 2024')
print('Welcome to SAPPERLOT - Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool\n')


main()