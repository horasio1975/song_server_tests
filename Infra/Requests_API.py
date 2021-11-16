import json
import requests


class RequestsApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = requests.Session()

    def _observe_response(self, response):
        print(f'response status code: {response.status_code}')
        print(f'response json: {response.json()}')
        return response.json()

    def get(self, url, input_data):
        return self._observe_response(self.session.get(self.base_url+url, params=input_data, headers=self.headers))

    def post(self, url, input_data):
        return self._observe_response(self.session.post(self.base_url+url, data=json.dumps(input_data),
                                                        headers=self.headers))

    def put(self, url, input_data):
        return self._observe_response(self.session.put(self.base_url+url, data=json.dumps(input_data),
                                                       headers=self.headers))

    def delete(self, url):
        return self._observe_response(self.session.delete(self.base_url+url, headers=self.headers))

