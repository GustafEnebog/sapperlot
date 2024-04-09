# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

# Import python built-in module math used for basic math operations like: square root, exponents etc.
import math

# Import statistics Library used to calculate basic statistic like: arithmetic mean, median, spread, bell curce and interpolate
import statistics

# Import NumPy https://numpy.org/doc/stable/user/absolute_beginners.html
import numpy as np

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

print(data)

-------------------------------------------------------------------------------