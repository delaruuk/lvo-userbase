import gspread
from oauth2client.service_account import ServiceAccountCredentials

def append_data_to_sheet(data):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('HA LVO Portal Database Logbook').sheet1
    sheet.append_row(data)