import requests

class ASRFileApi:
    def __init__(self, base_url, username, password, verify=True):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify
        self.token = None
        self.headers = None

    def login(self):
        resp = requests.post(f'{self.base_url}/api/v1/login', json={
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
        return requests.post(f'{self.base_url}/api/v1/logout', headers=self.headers, verify=self.verify)

    def create_subtitle_task(self, file_bytes, filename='test.mp3', title='Test', description='Test upload'):
        if not self.headers:
            return None
        files = {'audio': (filename, file_bytes, 'audio/mpeg')}
        data = {'sourceType': 2, 'title': title, 'description': description}
        return requests.post(f'{self.base_url}/api/v1/subtitle/tasks', headers=self.headers, files=files, data=data, verify=self.verify)

    def list_subtitle_tasks(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/subtitle/tasks', headers=self.headers, verify=self.verify)

    def get_models(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/models', headers=self.headers, verify=self.verify) 