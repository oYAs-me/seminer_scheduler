import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sheet_id
from pprint import pprint

from datetime import datetime

# 認証情報(2.1s)
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
# name_sheet = ws.worksheet('name')
# name_data = name_sheet.get_all_values()
# pprint(name_data)

schedules = {} # {name: [[m11,t11,w11,t11,f11],~~,[m21,t21,w21,t21,f21],~~,]}(0 or 1が入る)
raw_sheet = ws.worksheet('copied_sheet')
raw_ans = raw_sheet.get_all_values()
for l in raw_ans[1:]:
    name = l[1]
    sche = [] # schedulesに追加するscheのやつ
    for t in l[3:]: # 時間割を抽出するゾーン
        s = [0,0,0,0,0] # [Mon,Tue,Wed,Thu,Fri] 
        if t == '':
            sche.append(s)
            continue
        print(t)
        if '月曜' in t:
            s[0] = 1
        if '火曜' in t:
            s[1] = 1
        if '水曜' in t:
            s[2] = 1
        if '木曜' in t:
            s[3] = 1
        if '金曜' in t:
            s[4] = 1
        sche.append(s)
    schedules[name] = sche # schedulesに上の形式で追加する

pprint(schedules)
