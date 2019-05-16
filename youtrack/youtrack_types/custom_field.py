from youtrack.youtrack_types.youtrack_object import YouTrackObject


class CustomField(YouTrackObject):
    def to_json(self):
        super().to_json()