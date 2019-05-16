

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class IntelliSense(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        self.suggestions = []
        self.highlights = []
        self.queries = []
        super().__init__(data, youtrack)

    def to_json(self):
        super().to_json()

    def _update(self, xml):
        raise NotImplementedError
