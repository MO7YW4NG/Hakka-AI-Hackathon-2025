import requests

class TTSApi:
    def __init__(self, base_url, username, password, verify=True):
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

    def logout(self):
        if not self.headers:
            return None
        return requests.post(f'{self.base_url}/api/v1/tts/logout', headers=self.headers, verify=self.verify)

    def synthesize(self, text='你好', text_type='common', model='default', language_code='hak-xi-TW', name='hak-xi-TW-vs2-M01'):
        if not self.headers:
            return None
        payload = {
            'input': {'text': text, 'textType': text_type},
            'voice': {'model': model, 'languageCode': language_code, 'name': name},
            'audioConfig': {'speakingRate': 1.0},
            'outputConfig': {'streamMode': 0}
        }
        return requests.post(f'{self.base_url}/api/v1/tts/synthesize', headers=self.headers, json=payload, verify=self.verify)

    def get_models(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/tts/models', headers=self.headers, verify=self.verify)

    def get_text_type_options(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/tts/synthesize/text-type-options', headers=self.headers, verify=self.verify) 