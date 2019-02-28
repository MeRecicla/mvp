import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_name = "merecicla-sheet-teste"
credentials_file_path = './auth.json'
sheet_header_index = 1

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)
client = gspread.authorize(creds)
sheet = client.open(sheet_name).sheet1

def get_all_records():
    return sheet.get_all_records()

def get_record_by_row(row_index):
    record_array = sheet.row_values(row_index)
    return _format_record(record_array)

def get_record_by_column(column_index):
    record_array = sheet.col_values(column_index)
    return _format_record(record_array)

def get_cell_by_value(value):
    return sheet.find(value)

def insert_record(record):
    index = sheet_header_index + 1
    sheet.insert_row(record, index)

def delete_record(value):
    cell = get_cell_by_value(value)
    sheet.delete_row(cell.row)

def _format_record(record_values):
    record_titles = sheet.row_values(sheet_header_index)
    zipped_record = zip(record_titles, record_values)
    return dict(zipped_record)