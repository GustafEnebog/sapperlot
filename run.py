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

# Import pprint
from pprint import pprint

# Import python built-in module math used for basic math operations like: square root, exponents etc.
import math

# Import statistics Library used to calculate basic statistic like: arithmetic mean, median, spread, bell curce and interpolate
import statistics

# Module for search using regex
import re

# Import NumPy https://numpy.org/doc/stable/user/absolute_beginners.html
# import numpy as np

# NOTICE: The google sheets are formated (in the sheets, not in run.py) down to row 200, unsure if it is important but it might cause errors after this, simply copy a formated empty row and copy it onto rows past row 200 to format further!
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


def main_menu_select():
    """ Handles selection from main menu
    """
    print('\nMAIN MENU')
    print('1. Add data')
    print('2. Edit data')
    print('3. Delete data')
    print('4. View list of Airplane Categories')
    print('5. View data')
    print('6. Search data')
    print('7. Meta data')
    print('8. Bell curve')
    print('9. Inbetween points     "H" HELP     "Q" QUIT PROGRAM')

    while True:
        selection_main_menu = input('\nPlease select an option by entering a number between 1-9 an H or Q:\n')
        if selection_main_menu == '1':
            unconverted_airplane_data = get_airplane_data()
            converted_airplane_data = convert_to_int_and_float(unconverted_airplane_data)
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
            view_list_of_worksheets()
            break
        elif selection_main_menu == '5':
            select_and_view_airplane_data()
            break
        elif selection_main_menu == '6':
            search_data()
            break
        elif selection_main_menu == '7':
            calc_meta_data()
            break
        elif selection_main_menu == '8':
            create_bell_curve_graph()
            break
        elif selection_main_menu == '9':
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

            int(values[4])  # test if value f (year) can be converted into int
        for i in range(5, 10):  # 10 items in a list starting at index 0 running untill index 9
            float(values[i])  # test if fifth to tenth value can be converted into float
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def convert_to_int_and_float(unconverted_airplane_data):
    """ Converts the numeric data (year, wing_span, aspect_ratio, wing_area, max_takeoff_weight, wing_loading) to integers

    Argumemts: 
    Returns: 
    """
    # converted_airplane_data = unconverted_airplane_data  # Looks not so right but it made it work, at least at one point in time!
    #converted_airplane_data = []
    #converted_airplane_data[4] = int(unconverted_airplane_data[4])  # Entry of Year
    #for i in range(5, 10):
        # print(unconverted_airplane_data)
    #    converted_value[i] = float(unconverted_airplane_data[i])
    #    converted_airplane_data.append(converted_value)
    #    converted_airplane_data = format(converted_airplane_data[i], ".2f")  # Formate floats to two decimals. Note that it is truncated (all the decimals are still there under the hood), not rounded (that would be the round() function) 
    # return converted_airplane_data


    converted_airplane_data = unconverted_airplane_data  # Looks not so right but it made it work, at least at one point in time!
    converted_airplane_data[4] = int(unconverted_airplane_data[4])  # Entry of Year
    for i in range(5, 10):
        print(unconverted_airplane_data)
        converted_airplane_data[i] = float(unconverted_airplane_data[i])
        # converted_airplane_data = format(converted_airplane_data[i], ".2f")  # Formate floats to two decimals. Note that it is truncated (all the decimals are still there under the hood), not rounded (that would be the round() function) 
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


def create_worksheet():
    """ Edit the relevant worksheet with the data provided
    Create Worksheet
    You can create a new worksheet in the selected spreadsheet using the following command.
    """
    print('Please select an option by entering a number between 0-x:')
    # worksheet = sh.add_worksheet(title="A worksheet", rows="100", cols="20")


def edit_data():
    """ Edit the relevant worksheet with the data provided
    """
    print('Please select an option by entering a number between 0-x:')


def delete_data():
    """ Delete Worksheet
    You can delete a worksheet using the below given command and passing worksheet retrieved in "Select Worksheet".
    """
    # print('Please select an option by entering a number between 0-x:')
    # SHEET.del_worksheet(worksheet)

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


def view_list_of_worksheets():
    """
    selecs and collects columns of airplane data from worksheet,
    and returns the data as a list of lists.

    https://codingpub.dev/access-google-sheets-in-python-using-gspread/    
    """
    list_of_worksheets = SHEET.worksheets()
    print(list_of_worksheets)


def select_airplane_category():
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
        general_aviation_sheet = SHEET.worksheet("general_aviation").get_all_values()
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
    """
    search for search words in worksheet
    Credit to Code Institute tutor "John" for bugfix
    https://codingpub.dev/access-google-sheets-in-python-using-gspread/
    https://docs.gspread.org/en/latest/api/models/worksheet.html#gspread.worksheet.Worksheet.findall     middle of page
    """
    print('\nWhich category do you want to search?:')
    sheet_select = select_airplane_category()

    print('\n1. Exact word search')
    print('2. Regular expression (regex)     "M" MAIN MENU     "H" HELP     "Q" QUIT PROGRAM')
    select_value = input('\nPlease select an option by entering a number between 1-2 an H, M or Q:\n')

    cell = 'No results found'
    if select_value == '1':
        search_word = input('\nPlease enter an exact search word (not case sensitive):\n')
        # cell = worksheet.find('search_word')  # cell = worksheet.find("Mail")
        cell = SHEET.worksheet(sheet_select).find(search_word)
        # cell = find('search_word', case_sensitive=True)
    elif select_value == '2':
        search_word = input('\nPlease enter a word or a sequence of characters in the word you search for\n')
        regex = re.compile(rf'{search_word}')  #mail_re = re.compile(r'(Google|Yahoo) Mail')     cell = worksheet.find(mail_re)
        cell = SHEET.worksheet(sheet_select).findall(regex)
    elif select_value == 'H':
        help()
    elif select_value == 'M':
        main_menu_select()
    elif select_value == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')

    if cell != '':
        print(f'{search_word} exist in the worksheet in cell {cell}')
    elif cell == '':
        print(f'No sesults found for {search_word}')
    else:
        print('I guess one always should have an else-statement but what on earth should I write here!?')

def select_and_pull_airplane_data_from_worksheet():
    """
    selecs and collects columns of airplane data from worksheet,
    and returns the data as a list of lists.

    https://codingpub.dev/access-google-sheets-in-python-using-gspread/    
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()

    values_list = worksheet.col_values(1)
    sorted()



#6 - Get Cell Value
#You can get call value either using cell label or using cell coordinates with the commands given below

#val = worksheet.acell('B1').value # With label

#val = worksheet.cell(1, 2).value # With coords
#7 - Get all values from row or column
#If you want to values from an entire row or entire column you can use the following commands

#values_list = worksheet.row_values(1)

#values_list = worksheet.col_values(1)


def calc_mean():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://www.w3schools.com/python/ref_stat_mean.asp
    https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """


def calc_mean():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    https://www.w3schools.com/python/ref_stat_mean.asp
    https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    
    Argumemts: airplane_data_select_parameter[]
    Returns: mean value for airplane_data_select_parameter[]
    """
    values_list = SHEET.worksheet("multirole_fighter").col_values(1)
    print(values_list)
    sorted(values_list)
    print(values_list)
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


def calc_meta_data():
    """ Calculate mean (Arithmetic mean) for a parameter in airplane_data[].
    
    Argumemts: airplane_data_select_parameter[]
    Returns: 
    """
    values_list = SHEET.worksheet("airliner").col_values(5)
    print('printout before pop' + str(values_list))
    # using pop(0) to perform removal
    values_list.pop(0)
    print('printout after pop' + str(values_list))

    # converted_airplane_data = unconverted_airplane_data  # Looks not so right but it made it work, at least at one point in time!
    # converted_airplane_data[4] = int(values_lista[4])  # Entry of Year
    for i in range(len(values_list)):
    # for i in range(0, len(values_list)):
        values_list[i] = float(values_list[i])
        print(values_list)


    print('printout before sorted' + str(values_list))
    values_list = sorted(values_list)
    print('printout after sorted' + str(values_list))

    mean = statistics.mean(values_list)
    median = statistics.median(values_list)
    variance = statistics.variance(values_list)

    print(f'mean {mean} unit')
    print(f'mean {median} unit')
    print(f'mean {variance} unit')

    numpy.interp(x, xp, fp, left=None, right=None, period=None)[source]
    #print(values_list)
    #sorted(values_list)
    #print(values_list)
    # mean_of_year = print(statistics.mean(values_list))  # print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
    #print(mean_of_year)
    # numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)[source]
    
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

    Code snippet for "sorting a list using a second list" (approach 1) https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/

    https://numpy.org/doc/stable/reference/generated/numpy.interp.html

    Argumemts: x
    Returns: mean wing span value
    """


    
    # Selection of aircraft data parameter (y-coordinates) you wish to calculate an "inbetween"-value for, e.g. wing area.
    print('Aircraft data parameters (y-coord.) to calculate "inbetween"-value, e.g. wing area')
    print('1. Wing span')
    print('2. Aspect ratio')
    print('3. Wing area')
    print('4. Max takeoff weight')
    print('5. Wing loading')
    select_value_1 = input('\nPlease select an option by entering a number between 1-5 an H, M or Q:\n')

    if select_value_1 == '1':
        y_parameter_index = 5  # Wing span
    elif select_value_1 == '2':
         y_parameter_index = 6  # Aspect ratio
    elif select_value_1 == '3':
         y_parameter_index = 7  # Wing area
    elif select_value_1 == '4':
         y_parameter_index = 8  # Max takeoff weight
    elif select_value_1 == '5':
         y_parameter_index = 9  # Wing loading
    elif selection_sub_menu_dep_variable == 'H':
        help()
    elif selection_sub_menu_dep_variable == 'M':
        main_menu_select()
    elif selection_sub_menu_dep_variable == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')


    # Selection of aircraft data parameter (x-coordinates) to make the above selected parameter dependent on e.g. Max Takeoff Weight. These values must be increasing.   
    print('Aircraft data parameters (x-coord.) to base calulation of "inbetween"-value, e.g. Max Takeoff Weight. You may not select the same parameter as already selected in previous step\n')
    print('1. Wing span')
    print('2. Aspect ratio')
    print('3. Wing area')
    print('4. Max takeoff weight')
    print('5. Wing loading')
    select_value_2 = input('\nPlease select an option by entering a number between 1-5 an H, M or Q:\n')

    if select_value_2 == select_value_1:
        print('Invalid choice, You may not chose the same parameter as you made in your previous selection (y-coord.) 1-3 an H, M or Q:\n')
    elif select_value_2 == '1':
        x_parameter_index = 5  # Wing Span
        print_parameter = 'Wing span'
    elif select_value_2 == '2':
        x_parameter_index = 6  # Aspect Ratio
        print_parameter = 'Aspect ratio'
    elif select_value_2 == '3':
        x_parameter_index = 7  # Wing Area
        print_parameter = 'Wing area'
    elif select_value_2 == '4':
        x_parameter_index = 8  # Max Takeoff Weight
        print_parameter = 'Max Takeoff Weight'
    elif select_value_2 == '5':
        x_parameter_index = 9  # Wing Loading
        print_parameter = 'Wing loading'
    elif selection_sub_menu_dep_variable == 'H':
        help()
    elif selection_sub_menu_dep_variable == 'M':
        main_menu_select()
    elif selection_sub_menu_dep_variable == 'Q':
        os.abort()  #Abort the current running process
    else:
        print('Invalid choice, please enter a number between 1-3 an H, M or Q:\n')


    # Selection of the value (of the above selected aircraft data parameter, x-coordinates) at which to evaluate the interpolated value.
    print('Note in the case of extrapolation that the reliability of estimate\nquickly deteriate as estimates moves away from the outermost data points')
    x_value = input('\nPlease select an value of "' + str(print_parameter) + '" to interpolate, e.g. 16500 kg:\n')

    print('y_parameter_index "' + str(y_parameter_index) + '" x_parameter_index "' + str(x_parameter_index) + '" x_value "' + str(x_value) + '"')



    # Get correct list for popping, transform to floats, sorting and then interpolating
    values_list_y = SHEET.worksheet("multirole_fighter").col_values(y_parameter_index)
    values_list_x = SHEET.worksheet("multirole_fighter").col_values(x_parameter_index)

    #values_list = worksheet.col_values(1)
    print(values_list_y)
    print(values_list_x)
    while True:
        break
    sorted(values_list)
    print(values_list)


    values_list = SHEET.worksheet("airliner").col_values(5)
    print('printout before pop' + str(values_list))
    # using pop(0) to perform removal
    values_list.pop(0)
    print('printout after pop' + str(values_list))



    # Python program to sort one list using the other list
    def sort_list(list1, list2):
        zipped_pairs = zip(list2, list1)
        z = [x for _, x in sorted(zipped_pairs)]
        return z

    # driver code
    x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
    print(sort_list(x, y))

    x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
    y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
    print(sort_list(x, y))




    # numpy.interp(x, xp, fp, left=None, right=None, period=None)[source]
    # Note - The datas independent variable needs to be sorted so that it is increasing!

    print("testing...\n")
    # xxxxx = SHEET.worksheet("multirole_fighter").get_all_values()

    #values_list = worksheet.col_values(1)
    #values_list = airliner.col_values(1)
    # values_list = aircraft_data.col_values(1)
    # values_list = SHEET.worksheet('multirole_fighter')  col_values(1)
    # values_list = SHEET.airliner.col_values(1)
    #values_list = airliner.aircraft_data.col_values(1)
    #values_list = aircraft_data.airliner.col_values(1)
    #values_list = SHEET.airliner.col_values(1)
 

    # converted_airplane_data = unconverted_airplane_data  # Looks not so right but it made it work, at least at one point in time!
    # converted_airplane_data[4] = int(values_lista[4])  # Entry of Year
    for i in range(len(values_list)):
    # for i in range(0, len(values_list)):
        values_list[i] = float(values_list[i])
        print(values_list)


    print('printout before sorted' + str(values_list))
    values_list = sorted(values_list)
    print('printout after sorted' + str(values_list))

    mean = statistics.mean(values_list)
    median = statistics.median(values_list)
    variance = statistics.variance(values_list)

    print(f'mean {mean} unit')
    print(f'mean {median} unit')
    print(f'mean {variance} unit')

    numpy.interp(x, xp, fp, left=None, right=None, period=None)[source]
    #print(values_list)
    #sorted(values_list)
    #print(values_list)
    # mean_of_year = print(statistics.mean(values_list))  # print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
    #print(mean_of_year)
    # numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)[source]
    
    print("Meta data - Please select an option by entering a number between 0-x:")













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

print('\033[1;34;40m \n\nx x x x      x      x x x x   x x x x   x x x x   x x x x   x         x x x x   x x x x')
print('x           x x     x     x   x     x   x         x     x   x         x     x      x')
print('x x x x    x   x    x x x x   x x x x   x x x x   x x x x   x         x     x      x')
print('      x   x x x x   x         x         x         x   x     x         x     x      x')
print(f'x x x x  x       x  x         x         x x x x   x     x   x x x x   x x x x      x\n{Colors.ENDC}\n')


# Welcome message
print(f'{Colors.BLUE}\nx x x x      x      x x x x   x x x x   x x x x   x x x x   x         x x x x   x x x x')
print('x           x x     x     x   x     x   x         x     x   x         x     x      x')
print('x x x x    x   x    x x x x   x x x x   x x x x   x x x x   x         x     x      x')
print('      x   x x x x   x         x         x         x   x     x         x     x      x')
print(f'x x x x  x       x  x         x         x x x x   x     x   x x x x   x x x x      x{Colors.ENDC}\n')

# print(f'{Colors.BLUE}\n                                        ')
# print('                                               ')
# print('                                        ')
# print('                                               ')
# print('                                          {Colors.ENDC}\n')

# print(f'{Colors.BLUE}\nI I I     I     I I I  I I I  I I I  I I I  I      I I I  I I I')
# print('I        I I    I   I  I   I  I      I   I  I      I   I    I')
# print('I I I   I   I   I I I  I I I  I I I  I I I  I      I   I    I')
# print('    I  I I I I  I      I      I      I I    I      I   I    I')
# print('I I I  I     I  I      I      I I I  I   I  I I I  I I I    I{Colors.ENDC}\n')

print('Welcome to SAPPERLOT -              Copyright: Gustaf Enebog 2024') # Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool\n')
print('Statistical Airplane Potent Parameter Engineering Radical Loaded Oranges Tool\n')

main()




# Format these nely calculated dependent values to two decimals
    #for i in range(5, 10):
        # airplane_data = format(airplane_data[i], ".2f")  # Formate floats to two decimals. Note that it is truncated (all the decimals are still there under the hood), not rounded (that would be the round() function) 