

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Role(YouTrackObject):
    def to_json(self):
        super().to_json()
