import gspread
import json

from config import URL_GOOGLE_SHEETS


def add_data_table(data):
    try:
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)
            gc = gspread.service_account_from_dict(credentials)
            sheet = gc.open_by_url(URL_GOOGLE_SHEETS).sheet1
            sheet.append_row(data)
    except FileNotFoundError:
        print('Файл отсутствует')
