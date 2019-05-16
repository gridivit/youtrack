from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Link(YouTrackObject):
    type_name = ''
    source = ''
    target = ''

    def to_json(self):
        super().to_json()

    def __hash__(self):
        return hash((self.type_name, self.source, self.target))

    def __eq__(self, other):
        return isinstance(other, Link) and \
               self.type_name == other.type_name and self.source == other.source and self.target == other.target

    def __ne__(self, other):
        return not self.__eq__(other)
