from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Comment(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.author = ''
        super().__init__(data, youtrack)
        if not hasattr(self, 'text'):
            self.text = ''

    def to_json(self):
        super().to_json()

    def get_author(self):
        raise NotImplementedError
