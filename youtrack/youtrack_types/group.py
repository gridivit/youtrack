from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Group(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.name = ''
        super().__init__(data, youtrack)

    def to_json(self):
        super().to_json()
