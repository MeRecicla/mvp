import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheet_name = "ME RECICLA - Relação de objetos e categorias"
credentials_file_path = './auth.json'
sheet_header_index = 1

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)
client = gspread.authorize(creds)
sheet = client.open(sheet_name).sheet1

def get_all():
    return sheet.get_all_records()

def get_by_name(object_name):
    records = get_all()
    for obj in records:
        if object_name in obj['nome']:
            return obj
    return None

def get_category(object_name):
    obj = get_by_name(object_name)
    if(obj):
        return obj['categoria']
    else:
        return None

def insert_record(record):
    index = sheet_header_index + 1
    sheet.insert_row(record, index)

def delete_record(value):
    cell = __get_cell_by_value(value)
    sheet.delete_row(cell.row)

def __get_cell_by_value(value):
    return sheet.find(value)