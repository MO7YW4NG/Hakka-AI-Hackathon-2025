import requests

class TranslateApi:
    def __init__(self, base_url, username, password, verify=False):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify
        self.token = None
        self.headers = None

    def login(self):
        resp = requests.post(f'{self.base_url}/api/v1/tts/login', json={
            'username': self.username,
            'password': self.password
        }, verify=self.verify)
        if resp.ok and 'token' in resp.json():
            self.token = resp.json()['token']
            self.headers = {'Authorization': f'Bearer {self.token}'}
        return resp

    def translate_zh_to_hakka_hanzi(self, text):
        if not self.headers:
            return None
        payload = {'input': text}
        return requests.post(f'{self.base_url}/MT/translate/hakka_zh_hk', headers=self.headers, json=payload, verify=self.verify) 