class YouTrackBroadException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(msg)


class LogicException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
