from youtrack.youtrack_types.you_track_error import YouTrackError

class YouTrackBroadException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(msg)


class LogicException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class YouTrackException(Exception):
    def __init__(self, url, response, content):
        self.response = response
        self.content = content
        msg = 'Error for [' + url + "]: " + str(response.status)

        if response.reason is not None:
            msg += ": " + response.reason

        if 'content-type' in response:
            ct = response["content-type"]
            if ct is not None and ct.find('text/html') == -1:
                try:
                    self.error = YouTrackError(content, self)
                    msg += ": " + self.error.error
                except YouTrackBroadException:
                    self.error = content
                    msg += ": " + self.error

        super().__init__(msg)
