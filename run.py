# Heroku terminal 80 char wide, 24 rows high
# PEP8 code 79 char wide (72 for comments)
#----------------------------------------------------------------------*------**
# Run program: python3 run.py

import gspread
from google.oauth2.service_account import Credentials

#Import OS Library
import os

# Import colorama for colored command line text (slightly below middle of page)
# https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python#:~:text=You%20can%20use%20the%20Colorama,for%20colored%20text%20in%20Python.
#  ANSI escape codes. and/with colorama python library
# I installed colorama with the following command (type in command line):
# - pip3 install colorama for Python 3 and pip install colorama for
# older versions of Python
from colorama import Fore

# Import pprint
from pprint import pprint

# Import python built-in module math used for basic math operations like:
# square root, exponents etc.
import math

# Import statistics Library used to calculate basic statistic like:
# arithmetic mean, median, spread, bell curce and interpolate
import statistics

# Module for search using regex
import re

# Used for interpolation in function: calc_inbetween_outside_point()
import numpy

# Import NumPy https://numpy.org/doc/stable/user/absolute_beginners.html
# import numpy as np

# NOTICE: The google sheets are formated (in the sheets, not in run.py) down to
# row 200, unsure if it is important but it might cause errors after this,
# simply copy a formated empty row and copy it onto rows past row 200
# to format further!

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('aircraft_data')

class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    YELLOW = '\u001b[33m'
    RED = '\033[91m'
    BLACK = '\u001b[30m'
    ENDC = '\033[0m'


def esc(code):
    """ Function somehow necessary for colorama
    """
    return f'\033[{code}m'

#----------------------------------------------------------------------*------**
def get_airplane_data():
    """ Get and validate (via function call) inputed airplane data.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 10 items separated
    by commas (str,str,str,str,int,float,float,float,float,float).
    The loop will repeatedly request data, until it is valid.

    Based on "get_sales_data()" in loveSandwiches, AJGreaves at Code Institute
    https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1
    
    function calls: validate_airplane_data(values)
    Returns: airplane_data list (str, int and float) - 
    incomplete user input data for one airplane.
    """
    # Sub menu - FIRST choise
    print('\nSets of Aircraft parameters to input (S̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶ parameters will be calculated for you!)')
    print('1. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('2. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, Wing area, Max takeoff weight, '  + esc('238;2;9') + 'Wing loading' + esc(0))
    print('3. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('4. Wing span, ' + esc('238;2;9') + 'Aspect ratio,' + esc(0) + ' Wing area, Max takeoff weight, ' + esc('238;2;9') + 'Wing loading'  + esc(0))
    print('5. ' + esc('238;2;9') + 'Wing span,' + esc(0) + ' Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight, Wing loading')
    print('6. Wing span, ' + esc('238;2;9') + 'Aspect ratio,'  + esc(0) + ' ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' Max takeoff weight'  + esc(0) + ', Wing loading')
    print('7. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,'  + esc(0) + ' ' + esc('238;2;9') + 'Max takeoff weight,'  + esc(0) + ' Wing loading')
    print('8. Wing span, Aspect ratio, ' + esc('238;2;9') + 'Wing area,' + esc(0) + ' Max takeoff weight, ' + esc('238;2;9') + 'Wing loading'  + esc(0))
    print('"H" HELP             "M" BACK TO MAIN MENU             "Q" QUIT PROGRAM')

    global selection_sub_menu_dep_variable
    while True:
        selection_sub_menu_dep_variable = input('\nPlease select an alternative by entering a number between 1-8 an H, M or Q:\n')
        if selection_sub_menu_dep_variable == '1':
            print('\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio[n/a], wing_area[m\u00b2], 0, wing_loading[kg/m\u00b2] \n(give "0" as placeholder for "Wing span" and "Max Takeoff Weight".)\n')
            break
        elif selection_sub_menu_dep_variable == '2':
            print('\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio[n/a], wing_area[m\u00b2], max_takeoff_weight[kg], 0 \n(give "0" as placeholder for "Wing span" and "Wing loading".)\n')
            break
        elif selection_sub_menu_dep_variable == '3':
            print('\nairplane_name, manufacturer, country, category, year, wing_span[m], 0, wing_area[m\u00b2], 0, \n(give "0" as placeholder for "Aspect Ratio" and "Max Takeoff Weight".)\n')
            break
        elif selection_sub_menu_dep_variable == '4':
            print('\nairplane_name, manufacturer, country, category, year, wing_span[m], 0, wing_area[m\u00b2], max_takeoff_weight[kg], 0 \n(give "0" as placeholder for "Aspect Ratio" and "Wing loading".)\n')
            break
        elif selection_sub_menu_dep_variable == '5':
            print('\nairplane_name, manufacturer, country, category, year, 0, aspect_ratio[n/a], 0, max_takeoff_weight[kg], wing_loading[kg/m\u00b2] \n(give "0" as placeholder for "Wing span" and "Wing Area".)\n')
            break
        elif selection_sub_menu_dep_variable == '6':
            print('\nairplane_name, manufacturer, country, category, year, wing_span[m], 0, 0, max_takeoff_weight[kg], wing_loading[kg/m\u00b2] \n(give "0" as placeholder for "Aspect Ratio" and "Wing Area".)\n')
            break 
        elif selection_sub_menu_dep_variable == '7':
            print('\nairplane_name, manufacturer, country, category, year, wing_span[m], aspect_ratio[n/a], 0, 0, wing_loading[kg/m\u00b2] \n(give "0" as placeholder for "Wing Area" and "Max Takeoff Weight".)\n')
            break
        elif selection_sub_menu_dep_variable == '8':
            print('\nairplane_name, manufacturer, country, category, year, wing_span, aspect_ratio[n/a], 0, max_takeoff_weight, 0 \n(give "0" as placeholder for "Wing Area" and "Wing loading".)\n')
            break
        elif selection_sub_menu_dep_variable == 'H':
            help()
            break
        elif selection_sub_menu_dep_variable == 'M':
            main_menu_select()
            break
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
    Validates if user input is valid by trying to convert data types
    (str, int and float), if there is exactly 10 values
    and that they are all positive and larger than zero.

    Inside the try, converts the fifth to int and sixth to tenth to integers
    (however only test, it keeps the data with its old types).
    Raises ValueError if these strings cannot be converted,
    or if there aren't exactly 10 values.

    Based on "validate_data()" in loveSandwiches, AJGreaves at Code Institute
    https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1
    
    Argumemts: values - incomplete user input data for one airplane.
    Returns: true or false
    """
    try:
        if len(values) != 10:  # 10 items in a list starting at index 0 running untill index 9
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
            int(values[4])  # test if value f (year) can be converted into int
        for i in range(5, 10):  # 10 items in a list starting at index 0 running untill index 9
            float(values[i])  # test if fifth to tenth value can be converted into float
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def convert_to_int_and_float(unconverted_airplane_data):
    """ Converts the str data to integers and floats
    Before conversion: (str,str,str,str,str,str,str,str,str,str)
    After conversion: (str,str,str,str,int,float,float,float,float,float)
    (year, wing_span, aspect_ratio, wing_area, max_takeoff_weight, wing_loading)

    Arguments: unconverted_airplane_data
    Returns: converted_airplane_data
    """
    converted_airplane_data = unconverted_airplane_data
    converted_airplane_data[4] = int(unconverted_airplane_data[4])  # Entry of Year
    for i in range(5, 10):
        converted_airplane_data[i] = float(unconverted_airplane_data[i])
    return converted_airplane_data


def uppdate_dependent_airplane_data(converted_airplane_data):
    """ Calculates and fills in dependent values (inputted with placeholder '0')
    using equations using the inputed values.
    If user would input all values it would over-define (overdetermine) the
    airplane-data.
    Based on "update_worksheet()" in loveSandwiches, AJGreaves at Code Institute
    https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1

    https://docs.google.com/spreadsheets/d/186F_QSx24xYlkzunnzrzawt06MJO8GfdPsxGeRoqIa4/edit#gid=1680754323

    Argumemts: converted_airplane_data
    Returns: airplane_data
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
    
    for i in range(5, 10):
        airplane_data[i] = format(airplane_data[i], ".2f")

    return airplane_data


def push_airplane_data_to_worksheet(data):  # loveSandwiches code also have a worksheet as an argument. I took it away since it does not work since it is not defined
    """ Update the correct tab in worksheet with data in the form of
    a list of string, integer and float values

    Arguments: data
    """
    if data[3] == 'multirole_fighter':
        worksheet_to_update = SHEET.worksheet('multirole_fighter')
        worksheet_to_update.append_row(data)
        print('The "multirole_fighter"-category/tab in our worksheet updated successfully\n')
    elif data[3] == 'airliner':
        worksheet_to_update = SHEET.worksheet('airliner')
        worksheet_to_update.append_row(data)
        print('The "airliner"-category/tab in our worksheet updated successfully\n')
    elif data[3] == 'general_aviation':
        worksheet_to_update = SHEET.worksheet('general_aviation')
        worksheet_to_update.append_row(data)
        print('The "general_aviation"-category/tab in our worksheet updated successfully\n')
    else:
        print('Ouuups, you must have misspelled the fourth entry (category). \nIt should be multirole_fighter, airliner or general_aviation. sorry, but this error really should have been caught earlier!') # See if this erro can be checked earlier!!!


def post_select():
    """ Gives the user short menu post a request have been carried out
    """
    while True:
        print('\nH - Help')
        print('M - Main Menu')
        print('Q - Quit')
        select = input('\nPlease select an alternative by entering H, M or Q:\n')
        if select == 'H':
            help()
            break
        elif select == 'M':
            main()
            break
        elif select == 'Q':
            os.abort()  #Abort the current running process
        else:
            print('Invalid choice, please select an alternative by entering H, M or Q:\n')
            continue


def add_data():
    """ Run all 'option 1. add-data' - functions

    Lifecycle of the user input:
    inputted_airplane_data -> unconverted_airplane_data -> converted_airplane_data -> airplane_data
    function calls: get_airplane_data()
                    convert_to_int_and_float()
                    uppdate_dependent_airplane_data()
                    push_airplane_data_to_worksheet()
    """
    unconverted_airplane_data = get_airplane_data()  # row 108
    converted_airplane_data = convert_to_int_and_float(unconverted_airplane_data)  # row 211
    airplane_data = uppdate_dependent_airplane_data(converted_airplane_data)   # row 237
    push_airplane_data_to_worksheet(airplane_data)  # row 299 loveSandwiches code also have a worksheet as an argument. I took it away since it does not work since it is not defined


def view_list_of_worksheets():
    """ Displays all sheets (categories) in the worksheets

    https://codingpub.dev/access-google-sheets-in-python-using-gspread/   
    
    function calls: validate_airplane_data(values)
    """
    list_of_worksheets = SHEET.worksheets()
    print(f'\n{list_of_worksheets}')


def select_airplane_category():
    """ Allows user to select sheet in worksheet and save selection in variable sheet_select
    
    Returns: sheet_select
    """
    print('1. Multirole fighter')
    print('2. Airliner')
    print('3. General Aviation')
    select_value = input('\nPlease select an option by entering a number between 1-3 an H, M or Q:\n')

    if select_value == '1':
        sheet_select = 'multirole_fighter'
    elif select_value == '2':
        sheet_select = 'airliner'
    elif select_value == '3':
        sheet_select = 'general_aviation'
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')
    
    return sheet_select


def select_and_view_airplane_data():
    """
    selecs and collects columns of airplane data from worksheet,
    and returns the data as a list of lists.

    https://codingpub.dev/access-google-sheets-in-python-using-gspread/
    """
    print('\n1. multirole_fighter')
    print('2. airliner')
    print('3. general aviation     "M" MAIN MENU     "H" HELP     "Q" QUIT PROGRAM')
    select_value = input('\nPlease select an option by entering a number between 1-3 an H, M or Q:\n')
    if select_value == '1':
        multirole_fighter_sheet = SHEET.worksheet("multirole_fighter").get_all_values()
        pprint(multirole_fighter_sheet)
    elif select_value == '2':
        airliner_sheet = SHEET.worksheet("airliner").get_all_values()
        pprint(airliner_sheet)
    elif select_value == '3':
        general_aviation_sheet = SHEET.worksheet("general_aviation").get_all_values()  # Why does this row not work
        pprint(general_aviation_sheet)
    elif select_value == 'H':
        help()
    elif select_value == 'M':
        main_menu_select()
    elif select_value == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')


def search_data():
    """ search for search words in worksheet
    Credit to Code Institute tutor "John" for bugfix
    https://codingpub.dev/access-google-sheets-in-python-using-gspread/
    https://docs.gspread.org/en/latest/api/models/worksheet.html#gspread.worksheet.Worksheet.findall (middle of page)

    Functions: select_airplane_category()
    Returns: sheet_select
    """
    print('\nWhich category do you want to search?:')
    sheet_select = select_airplane_category()

    print('\n1. Exact word search')
    print('2. Regular expression (regex)     "M" MAIN MENU     "H" HELP     "Q" QUIT PROGRAM')
    select_value = input('\nPlease select an option by entering a number between 1-2 an H, M or Q:\n')

    cell = 'No results found'
    if select_value == '1':
        search_word = input('\nPlease enter an exact search word (not case sensitive):\n')
        cell = SHEET.worksheet(sheet_select).find(search_word)
    elif select_value == '2':
        search_word = input('\nPlease enter a word or a sequence of characters in the word you search for\n')
        regex = re.compile(rf'{search_word}')
        cell = SHEET.worksheet(sheet_select).findall(regex)
    elif select_value == 'H':
        help()
    elif select_value == 'M':
        main_menu_select()
    elif select_value == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')

    # Handling of case when search word is not found
    if cell != '':
        print(f'{search_word} exist in the worksheet in cell {cell}')
    elif cell == '':
        print(f'No sesults found for {search_word}')
    else:
        print('I guess one always should have an else-statement but what on earth should I write here!?')


def calc_meta_data():
    """ Calculate 'mean' (Arithmetic mean) 'median' and 'variance' for each
    parameter in each aircraft category.
    The function gets the data directly from the worksheet
    
    https://www.w3schools.com/python/ref_stat_mean.asp
    https://www.w3schools.com/python/ref_stat_median.asp
    https://www.w3schools.com/python/ref_stat_variance.asp
    """
    sheets_for_loop =  ['multirole_fighter', 'airliner', 'general_aviation']
    for i in range(len(sheets_for_loop)):
        for j in range(6,10):
            values_list = SHEET.worksheet(sheets_for_loop[i]).col_values(j)
            # using pop(0) to remove table headline
            values_list.pop(0)
            for k in range(len(values_list)):
                # using float to convert str to float
                values_list[k] = float(values_list[k])
            # using math.statistics module 
            mean = statistics.mean(values_list)
            median = statistics.median(values_list)
            variance = statistics.variance(values_list)
            mean = format(mean, ".2f")
            median = format(median, ".2f")
            variance = format(variance, ".2f")
            # Print out calculated meta data
            if j == 6:
                print(f'\nMean "Wing Span" for {sheets_for_loop[i]}s are {mean} m')
                print(f'Median "Wing Span" for {sheets_for_loop[i]}s are {median} m')
                print(f'Variance for the "Wing Span" for {sheets_for_loop[i]}s is {variance} m')
            elif j == 7:
                print(f'\nMean "Aspect Ratio" for {sheets_for_loop[i]}s are {mean} n/a')
                print(f'Median "Aspect Ratio" for {sheets_for_loop[i]}s are {median} n/a')
                print(f'Variance for the "Aspect Ratio" for {sheets_for_loop[i]}s is {variance} n/a')
            elif j == 8:
                print(f'\nMean "Wing Area" for {sheets_for_loop[i]}s are {mean} m\u00b2')
                print(f'Median "Wing Area" for {sheets_for_loop[i]}s are {median} m\u00b2')
                print(f'Variance for the "Wing Area" for {sheets_for_loop[i]}s is {variance} m\u00b2')
            elif j == 9:
                print(f'\nMean "Max Takeoff Weight" for {sheets_for_loop[i]}s are {mean} kg')
                print(f'Median "Max Takeoff Weight" for {sheets_for_loop[i]}s are {median} kg')
                print(f'Variance for the "Max Takeoff Weight" for {sheets_for_loop[i]}s is {variance} kg')
            elif j == 10:
                print(f'\nMean "Wing Loading" for {sheets_for_loop[i]}s are {mean} kg/m\u00b2')
                print(f'Median "Wing Loading" for {sheets_for_loop[i]}s are {median} kg/m\u00b2')
                print(f'Variance for the "Wing Loading" for {sheets_for_loop[i]}s is {variance} kg/m\u00b2')
            else:
                print('\nindex error')


def calc_inbetween_outside_point():
    """ Calculate (interpolate or extrapolate) a value (inbetween the data points
    in aircraft_data).

    Code snippet for "sorting a list using a second list" (approach 1) 
    https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/
    Code for interpolate
    https://numpy.org/doc/stable/reference/generated/numpy.interp.html

    Returns: answer_y_value
    """
    # Code for getting the correct list--------------------------------------------------
    print('\nWhich category do you want to search?:')
    sheet_select = select_airplane_category()

    # USER INPUT - Selection of aircraft data parameter (y-coordinates) you wish to calculate
    # an "inbetween"-value for, e.g. wing area.
    print('\nAircraft data parameters (y-coord.) to calculate "inbetween"-value, e.g. wing area')
    print('1. Wing span')
    print('2. Aspect ratio')
    print('3. Wing area')
    print('4. Max takeoff weight')
    print('5. Wing loading')
    select_value_1 = input('\nPlease select an option by entering a number between 1-5 an H, M or Q:\n')

    if select_value_1 == '1':
        y_parameter_index = 6
        y_parameter_print = 'Wing span'
    elif select_value_1 == '2':
        y_parameter_index = 7
        y_parameter_print = 'Aspect ratio'
    elif select_value_1 == '3':
        y_parameter_index = 8
        y_parameter_print = 'Wing area'
    elif select_value_1 == '4':
        y_parameter_index = 9
        y_parameter_print = 'Max takeoff weight'
    elif select_value_1 == '5':
        y_parameter_index = 10
        y_parameter_print = 'Wing loading'
    elif selection_sub_menu_dep_variable == 'H':
        help()
    elif selection_sub_menu_dep_variable == 'M':
        main_menu_select()
    elif selection_sub_menu_dep_variable == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')


    # USER INPUT - Selection of aircraft data parameter (x-coordinates) to make the above
    # selected parameter dependent on e.g. Max Takeoff Weight.
    # These values must be increasing.   
    print('\nAircraft data parameters (x-coord.) to base calulation of "inbetween"-value, e.g. Max Takeoff Weight. You may not select the same parameter as already selected in previous step\n')
    print('1. Wing span')
    print('2. Aspect ratio')
    print('3. Wing area')
    print('4. Max takeoff weight')
    print('5. Wing loading')
    select_value_2 = input('\nPlease select an option by entering a number between 1-5 an H, M or Q:\n')

    if select_value_2 == select_value_1:
        print('Invalid choice, You may not chose the same parameter as you made in your previous selection (y-coord.) 1-3 an H, M or Q:\n')
    elif select_value_2 == '1':
        x_parameter_index = 6
        x_parameter_print = 'Wing Span'
    elif select_value_2 == '2':
        x_parameter_index = 7
        x_parameter_print = 'Aspect Ratio'
    elif select_value_2 == '3':
        x_parameter_index = 8
        x_parameter_print = 'Wing Area'
    elif select_value_2 == '4':
        x_parameter_index = 9
        x_parameter_print = 'Max Takeoff Weight'
    elif select_value_2 == '5':
        x_parameter_index = 10
        x_parameter_print = 'Wing Loading'
    elif selection_sub_menu_dep_variable == 'H':
        help()
    elif selection_sub_menu_dep_variable == 'M':
        main_menu_select()
    elif selection_sub_menu_dep_variable == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')


    # Fetch list and "pop"-away first index---------------------------------------
    # Get correct list for popping, transform to floats, sorting and then interpolating
  
    values_list_x = SHEET.worksheet(sheet_select).col_values(x_parameter_index)
    #print('printout "values_list_x"' + str(values_list_x))
    values_list_y = SHEET.worksheet(sheet_select).col_values(y_parameter_index)
    #print('printout "values_list_y"' + str(values_list_y))

    values_list_x.pop(0)
    values_list_y.pop(0)
    #print('printout "values_list_x POST POP"' + str(values_list_x))
    #print('printout "values_list_y POST POP"' + str(values_list_y))

# Sort list FIRST STAGE------------------------------------------------------------
    # Python program to sort one list using the other list
    values_list_x_for_zip = values_list_x
    values_list_y_for_zip = values_list_y
    zipped_pairs = zip(values_list_x_for_zip, values_list_y_for_zip)
    values_list_y_sort_1 = [x for _, x in sorted(zipped_pairs)]
    print('values_list_y_1_sort' + str(values_list_y_sort_1))

# Sort list SECOND STAGE------------------------------------------------------------
    values_list_x_sort_2 = sorted(values_list_x)
    print('values_list_x_2_sort' + str(values_list_x_sort_2))

# USER INPUT - Selection of the value (of the above selected aircraft data parameter,
    # x-coordinates) at which to evaluate the interpolated value.
    print('\nNote that the reliability of the estimated "inbetween"-value highly depend on the distance of this value to the data points in the set.\n especialy in the case of extrapolating (case of value outside of the datapoints)\nwhere the accuracy/reliability quickly deteriates as this value is chosen far away outside of data points')
    max_index = len(values_list_x_sort_2) - 1
    x_value = input('\nThe lowest data point is: ' + str(values_list_x_sort_2[0]) + '" and the uppermost data point is '  + str(values_list_x_sort_2[max_index]) + '\n')

# Interpolate/extrapolate-----------------------------------------------------------
    x = float(x_value)
    
    xp = values_list_x_sort_2
    for i in range(0, len(xp)):
        xp[i] = float(values_list_x_sort_2[i])
    print('xp' + str(xp))  # REMOVE LATER!!!!!!!!!!!!!!!!!!!!!!!

    fp = values_list_y_sort_1
    for i in range(0, len(fp)):
        fp[i] = float(values_list_y_sort_1[i])
    print('fp' + str(fp))   # REMOVE LATER!!!!!!!!!!!!!!!!!!!!!!!
    
    # Original: interpolated_y = numpy.interp(x, xp, fp, left=None, right=None, period=None)
    interpolated_y = numpy.interp(x, xp, fp)
    print('The ' + str(y_parameter_print) + '"-inbetween"-value, interpolated with respect to ' + str(x_parameter_print) + ', is: ' + str(interpolated_y))


def help():

    """ Display help text
    """
    print('\nHELP')
    print(f'Wing Span, m')
    print(f'Aspect Ratio, n/a')
    print(f'Wing Area, m\u00b2')
    print(f'Max Takeoff Weight, kg')
    print(f'Wing Loading, kg/m\u00b2')
   

def main():
    """ Run all program functions by running the main menu
    """
    print('\nMAIN MENU')
    print('1. Add data')
    print('2. View list of Airplane Categories')
    print('3. View data')
    print('4. Search data')
    print('5. Meta data')
    print('6. Inbetween points     "H" HELP     "Q" QUIT PROGRAM')

    while True:
        selection_main_menu = input('\nPlease select an option by entering a number between 1-9 an H or Q:\n')
        if selection_main_menu == '1':
            add_data()  # row 289
            break
        elif selection_main_menu == '2':
            view_list_of_worksheets()  # row 329
            break
        elif selection_main_menu == '3':
            select_and_view_airplane_data()  # row 358
            break
        elif selection_main_menu == '4':
            search_data()  # row 368
            break
        elif selection_main_menu == '5':
            calc_meta_data()  # row 457
            break
        elif selection_main_menu == '6':
            calc_inbetween_outside_point()  # row 509
            break
        elif selection_main_menu == 'H':
            help()
            break
        elif selection_main_menu == 'Q':
            os.abort()  #Abort the current running process
        else:
            print('Invalid choice, please enter a number between 1-6 an H or Q:\n')
            continue


# print('#----------------------------------------------------------------------*------**')

print('\nWelcome to SAPPERLOT -                          Copyright: Gustaf Enebog 2024')
print('Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool')

print('\033[1;34;40m\n\n                                ')
print('                                                    ')
print('                                   ')
print('                                                 ')
print(f'                                         \n{Colors.ENDC}\n')


main()