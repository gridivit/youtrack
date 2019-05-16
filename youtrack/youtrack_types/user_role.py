from youtrack.youtrack_types.youtrack_object import YouTrackObject


class UserRole(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.name = ''
        self.projects = []
        super().__init__(data, youtrack)

    def _update(self, data):
        raise NotImplementedError

    def to_json(self):
        raise NotImplementedError
