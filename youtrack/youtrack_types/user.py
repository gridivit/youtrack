from youtrack.youtrack_types.youtrack_object import YouTrackObject
from youtrack.helpers import cmp


class User(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.login = ''
        super().__init__(data, youtrack)
        self.get_groups = lambda: []

    def to_json(self):
        super().to_json()

    def __hash__(self):
        return hash(self.login)

    def __cmp__(self, other):
        if isinstance(other, User):
            return cmp(self.login, other.login)
        else:
            return cmp(self.login, other)