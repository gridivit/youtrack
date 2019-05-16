

from youtrack.youtrack_types.youtrack_object import YouTrackObject
from youtrack.exceptions import YouTrackException


class UserBundle(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.users = []
        self.groups = []
        super().__init__(data, youtrack)

    def _update(self, data):
        raise NotImplementedError

    def to_json(self):
        raise NotImplementedError

    @staticmethod
    def get_field_type():
        return "user"

    def get_all_users(self):
        raise NotImplementedError
