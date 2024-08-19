import gspread
from oauth2client.service_account import ServiceAccountCredentials

def append_data_to_sheet(data):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Your Spreadsheet').sheet1
    sheet.append_row(data)