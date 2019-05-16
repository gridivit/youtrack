from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Version(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        raise NotImplementedError

    def to_json(self):
        super().to_json()