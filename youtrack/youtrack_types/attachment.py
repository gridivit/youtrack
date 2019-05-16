import re

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Attachment(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.author_login = ''
        super().__init__(data, youtrack)
        # Workaround for JT-18936
        self['url'] = re.sub(r'^.*?(?=/_persistent)', '', self['url'])

    def to_json(self):
        super().to_json()

    def get_content(self):
        raise NotImplementedError

    def get_author(self):
        raise NotImplementedError
