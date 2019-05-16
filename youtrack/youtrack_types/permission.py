from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Permission(YouTrackObject):
    def to_json(self):
        raise NotImplementedError
