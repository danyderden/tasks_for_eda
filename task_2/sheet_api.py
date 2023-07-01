import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


def auth_to_google_sheet_api(cred_file: str):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        cred_file, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=http_auth)
    return service


def append_message_info_to_sheet(sheet_id: str, message_info: list, cred_file: str):
    service = auth_to_google_sheet_api(cred_file)
    service.spreadsheets().values().append(spreadsheetId=sheet_id, range='A1:C1',
                                           valueInputOption='RAW',
                                           body={'values': [message_info]}).execute()
