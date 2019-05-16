from youtrack.youtrack_types.youtrack_object import YouTrackObject


class ChangeField(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.name = None
        self.old_value = []
        self.new_value = []
        super().__init__(data, youtrack)

    def to_json(self):
        super().to_json()

    def _update(self, json):
        raise NotImplementedError
