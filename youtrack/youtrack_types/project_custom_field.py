from youtrack.youtrack_types.youtrack_object import YouTrackObject


class ProjectCustomField(YouTrackObject):
    def to_json(self):
        super().to_json()

    def _update_from_children(self, el):
        self.params = {}
        for c in el.getElementsByTagName('param'):
            name = c.getAttribute('name')
            value = c.getAttribute('value')
            self[name] = value
            self.params[name] = value
