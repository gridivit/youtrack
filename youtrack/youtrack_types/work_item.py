

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class WorkItem(YouTrackObject):
    def to_json(self):
        super().to_json()

    def _update(self, data):
        raise NotImplementedError
