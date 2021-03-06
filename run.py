import openpyxl
import gspread
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ] 

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('munster-tv')
# Balance sheet
balance = SHEET.worksheet('balance')

data = balance.get_all_values()

# Inventory sheet
inventory = SHEET.worksheet('inventory')
inv_file = inventory.get_all_values()

print(inv_file)


print(data)


