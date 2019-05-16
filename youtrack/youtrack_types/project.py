from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Project(YouTrackObject):
    def __init__(self, data=None, youtrack=None):
        raise NotImplementedError

    def to_json(self):
        super().to_json()

    def get_subsystems(self):
        raise NotImplementedError

    def create_subsystem(self, name, is_default, default_assignee_login):
        raise NotImplementedError