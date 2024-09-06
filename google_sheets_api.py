import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


def append_data_to_sheet(data):
    try:
        # Define the scope
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]

        # Get the path to the credentials file from an environment variable
        creds_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS", "your_credentials.json")

        # Authenticate using the service account credentials
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)

        # Open the Google Sheet
        sheet = client.open("HA LVO Portal Database Logbook").sheet1

        # Append the data to the first sheet
        sheet.append_row(data)

    except Exception as e:
        print(f"An error occurred: {e}")
