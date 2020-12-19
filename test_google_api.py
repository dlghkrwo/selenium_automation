import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
import pytest

class TestGoogleApi:
    
    @pytest.fixture
    def test_status_code(self):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
        client = gspread.authorize(creds)
        self.doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1jMSQCyB924dY34wfuCSAgnGQStFwz-n_Xlwja1RkMK8/edit#gid=0')
        
        response = requests.get("https://docs.google.com/spreadsheets/d/1jMSQCyB924dY34wfuCSAgnGQStFwz-n_Xlwja1RkMK8/edit#gid=0'")
        assert response.status_code == 200
        

    def test_write_sheet(self, test_status_code):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
        client = gspread.authorize(creds)
        self.doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1jMSQCyB924dY34wfuCSAgnGQStFwz-n_Xlwja1RkMK8/edit#gid=0')    
        # self.cnt = int(sheet1.cell(1, 2).value)
        print('number of rows', self.cnt)
        self.sheet1.insert_row(['hi', 'hello/babo/kyle', '0710', 'google.com'], 3)
        #insert_row = add a row in 3rd col

        self.sheet1.insert_row(['polly', 'oully'], 5)
        #add a row in 5th col

        self.sheet1.update_cell(1, 2, str(self.cnt + 1))
        # update_cell = edit a cell in location of 1,2

        self.sheet1.update_cell(5, 6, str(self.cnt +2))
        self.sheet1.update_cell(8, 9, str(self.cnt +2))



    

