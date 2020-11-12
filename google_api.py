import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)

doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1jMSQCyB924dY34wfuCSAgnGQStFwz-n_Xlwja1RkMK8/edit#gid=0')

sheet1 = doc.worksheet('sheet1')

cnt = int(sheet1.cell(1, 2).value)
print('number of rows', cnt)
sheet1.insert_row(['hi', 'hello/babo/kyle', '0710', 'google.com'], 3)
#insert_row = add a row in 3rd col

sheet1.insert_row(['polly', 'oully'], 5)
#add a row in 5th col

sheet1.update_cell(1, 2, str(cnt + 1))
# update_cell = edit a cell in location of 1,2

sheet1.update_cell(5, 6, str(cnt +2))
sheet1.update_cell(8, 9, str(cnt +2))