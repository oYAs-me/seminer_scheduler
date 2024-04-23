import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sheet_id
from pprint import pprint

# 認証情報
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY)
    return worksheet

jsonf = 'client_secret.json'
sheet_key = sheet_id.key
ws = connect_gspread(jsonf, sheet_key)

# ファイル確認

name_sheet = ws.worksheet('name')
name = name_sheet.get_all_values()
pprint(name)
