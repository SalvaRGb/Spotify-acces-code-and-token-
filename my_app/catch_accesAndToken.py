import requests
import base64
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

code_variable = None

with open('data_init.json') as json_file:
    acces_data = json.load(json_file)

class my_automate_request(BaseHTTPRequestHandler):
    '''Automate the https://accounts.spotify.com response by handle it with an HTTP server'''
    def do_GET(self):
        global code_variable
        self.close_connection = True
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        try:
            code_variable = query['code'][0]
        except KeyError as error:
            code_variable = 'Acces denied by user'

class acces_code ():

    def  __init__ (self):
        self.__my_scopes = ' '.join(acces_data['scopes'])
        self.__authorize_params = {
                    'client_id': acces_data['app_kew_words']['client_id'], 
                    'response_type': 'code',
                    'redirect_uri': f"http://{acces_data['server']}:{acces_data['port']}",
                    'scope': self.__my_scopes
                    }

    def get_acces_code(self):

        self.__my_acces_code_request_url = acces_data['authorize_base_url'] + acces_data['acces_code_endpoint']
        my_auth_request = requests.get(self.__my_acces_code_request_url, params = self.__authorize_params)
        authorization_response = my_auth_request.url
        complete_server_adress = (acces_data['server'], acces_data['port'])
        webbrowser.open_new_tab(authorization_response)
        my_server = HTTPServer(complete_server_adress, my_automate_request)
        my_server.handle_request()
        return code_variable

class token ():

        def  __init__ (self):

            self.__Authorization_byte_form = f"{acces_data['app_kew_words']['client_id']}:{acces_data['app_kew_words']['secret_id']}".encode()
            self.__client_credentials = base64.b64encode(self.__Authorization_byte_form)
            #for client credential code flow
            self.__token_params = {'grant_type': 'client_credentials'}
            self.__headers_params = {
                                'Authorization': f'Basic {self.__client_credentials.decode()}',
                                'Content-Type': 'application/x-www-form-urlencoded'
                                }
            #for authorization code flow (acces users)
            if code_variable != None:
                self.__token_params['grant_type'] = 'authorization_code'
                self.__token_params['code'] = code_variable
                self.__token_params['redirect_uri'] = f"http://{acces_data['server']}:{acces_data['port']}"

        def get_token (self):
            global code_variable
            self.__my_post = acces_data['authorize_base_url'] + acces_data['token_end_point']
            my_token_request = requests.post(self.__my_post, params = self.__token_params, headers = self.__headers_params)
            code_variable = None
            return  my_token_request.json()['access_token']