import json
import requests


def _observe_response(response):
    print(f'response json: {response.json()}')
    if response.status_code != 200:
        raise Exception(f'Error Status Code from server: {response.status_code}')
    return response.json()


class RequestsApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = requests.Session()

    def get(self, url, input_data):
        return _observe_response(self.session.get(self.base_url+url, params=input_data, headers=self.headers))

    def post(self, url, input_data):
        return _observe_response(self.session.post(self.base_url+url, data=json.dumps(input_data),
                                                        headers=self.headers))

    def put(self, url, input_data):
        return _observe_response(self.session.put(self.base_url+url, data=json.dumps(input_data),
                                                       headers=self.headers))

    def delete(self, url):
        return _observe_response(self.session.delete(self.base_url+url, headers=self.headers))

