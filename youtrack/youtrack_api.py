import json

from youtrack.connection import Connection


class YouTrackApi(Connection):

    def __init__(self, url, token, proxy_info=None, disable_ssl=False):
        default_headers = {'Content-Type': 'application/json; charset=UTF-8',
                           'accept': 'application/json'}
        response_data_formatter = json.loads

        super().__init__(url, token, proxy_info, disable_ssl, response_data_formatter, default_headers)