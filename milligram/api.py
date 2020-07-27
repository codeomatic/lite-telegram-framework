import requests


class Telegram:
    url_template = 'https://api.telegram.org/bot{token}/{method_name}'
    offset = 0

    def __init__(self, token):
        self.token = token

    def _post(self, method_name, **kwargs):
        resp = requests.post(
            self.url_template.format(token=self.token, method_name=method_name),
            json=kwargs
        )
        return resp.json()

    def get_me(self):
        return self._post('getMe')

    def list_updates(self):
        return self._post('getUpdates')

    def get_updates(self):
        resp = self._post('getUpdates', offset=self.offset)
        if not resp['ok']:
            return resp

        result = resp['result']
        if not result:
            return resp

        self.offset = result[-1]['update_id'] + 1
        return resp

    def get_web_hook_info(self):
        return self._post('getWebhookInfo')

    def delete_web_hook(self):
        return self._post('deleteWebhook')
