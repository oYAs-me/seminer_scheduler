import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sheet_id

# 認証情報
def connect_gspread():
    jsonf = 'client_secret.json'
    SPREADSHEET_KEY = sheet_id.key
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open_by_key(SPREADSHEET_KEY)
    return worksheet

# ファイル確認
def seminar_attendee(worksheet, seminar_name: str):
    name_sheet = worksheet.worksheet('name')
    name_data = name_sheet.get_all_values()
    for l in name_data[1:]:
        if l[0] == seminar_name:
            return [i for i in l[1:] if i != '']

def attendee_schedule(worksheet, attendee: list):
    # ↓ [[m11,t11,w11,t11,f11],~~,[m21,t21,w21,t21,f21],~~,]}(0 or 1が入る)
    schedules = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    raw_sheet = worksheet.worksheet('copied_sheet')
    raw_ans = raw_sheet.get_all_values()
    for l in raw_ans[1:]:
        name = l[1]
        if name in attendee:
            sche = [] # schedulesに追加するscheのやつ
            for t in l[3:]: # 時間割を抽出するゾーン
                s = [0,0,0,0,0] # [Mon,Tue,Wed,Thu,Fri] 
                if t == '':
                    sche.append(s)
                    continue
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
            schedules = [[x + y for x, y in zip(a, b)] for a, b in zip(schedules, sche)]
    return schedules
