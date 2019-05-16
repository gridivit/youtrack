import httplib2

import youtrack.exceptions


class Connection(object):
    def __init__(self, url, token, proxy_info=None, disable_ssl=False, response_formatter=None, default_headers=None):
        if proxy_info is None:
            self.http = httplib2.Http(disable_ssl_certificate_validation=disable_ssl)
        else:
            self.http = httplib2.Http(proxy_info=proxy_info, disable_ssl_certificate_validation=disable_ssl)

        self.response_formatter = response_formatter
        self.url = url
        self.base_url = url + "/rest"
        self.token = "Bearer {}".format(token)
        self.default_headers = default_headers

    def add_default_headers(self, headers: dict):
        self.default_headers.update(headers)

    def request(self, method, path, body=None, ignore_status=None, headers=None):
        header = dict()
        header.update(self.default_headers)
        if headers:
            header.update(headers)
        header["Authorization"] = self.token

        if method in ['PUT', 'POST']:
            headers['Content-Length'] = str(len(body)) if body else '0'

        response, content = self.http.request(self.base_url + path, method, headers=header, body=body)
        content = content.translate(None, '\0'.encode('utf-8'))

        if response.status != 200 and response.status != 201 and (ignore_status != response.status):
            raise youtrack.exceptions.YouTrackException(path, response, content)

        if self.response_formatter:
            content = self.response_formatter(content)

        return response, content

    def get(self, *args, **kwargs):
        return self.request("GET", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request("POST", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.request("PUT", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.request("DELETE", *args, **kwargs)
