

from youtrack.youtrack_types.youtrack_object import YouTrackObject
from youtrack.youtrack_types.change_field import ChangeField


class IssueChange(YouTrackObject):
    def __init__(self, json=None, youtrack=None):
        self.fields = []
        self.updated = 0
        self.updater_name = None
        self.comments = []
        super().__init__(json, youtrack)

    def to_json(self):
        super().to_json()

    def _update(self, xml):
        raise NotImplementedError
