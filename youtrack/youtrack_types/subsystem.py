from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Subsystem(YouTrackObject):
    def to_json(self):
        super().to_json()