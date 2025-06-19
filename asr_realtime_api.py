import requests
import websocket
import threading
import time
import urllib.parse

class ASRRealtimeApi:
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

    def get_streaming_access_info(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/streaming/transcript/access-info', headers=self.headers, verify=self.verify)

    def get_models(self):
        if not self.headers:
            return None
        return requests.get(f'{self.base_url}/api/v1/models', headers=self.headers, verify=self.verify)

    def connect_websocket(self, ws_url, ticket, **kwargs):
        """
        Connect to the real-time ASR websocket endpoint.
        ws_url: The websocket URL (from get_streaming_access_info)
        ticket: The ticket string (from get_streaming_access_info)
        kwargs: Additional query parameters (type, rate, channel, etc.)
        """
        # Build query string
        params = {'ticket': urllib.parse.quote(ticket)}
        params.update(kwargs)
        query = '&'.join(f"{k}={v}" for k, v in params.items())
        full_url = f"{ws_url}?{query}"

        def on_message(ws, message):
            print("[WebSocket] Received:", message)

        def on_error(ws, error):
            print("[WebSocket] Error:", error)

        def on_close(ws, close_status_code, close_msg):
            print("[WebSocket] Closed")

        def on_open(ws):
            print("[WebSocket] Connection opened")
            # Example: send a dummy message or audio data here if needed
            # ws.send(b'...')
            # For demo, close after a short wait
            def run():
                time.sleep(2)
                ws.close()
            threading.Thread(target=run).start()

        ws = websocket.WebSocketApp(full_url,
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever(sslopt={"cert_reqs": 0}) 