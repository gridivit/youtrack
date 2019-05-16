from youtrack.youtrack_types.youtrack_object import YouTrackObject
from youtrack.helpers import to_str
from youtrack.youtrack_types.attachment import Attachment
from youtrack.youtrack_types.link import Link


class Issue(YouTrackObject):
    def __init__(self, json=None, youtrack=None):
        raise NotImplementedError

    def to_json(self):
        super().to_json()

    def _normalize_multiple(self, name):
        raise NotImplementedError

    def get_reporter(self):
        raise NotImplementedError

    def has_assignee(self):
        raise NotImplementedError

    def get_assignee(self):
        raise NotImplementedError

    def get_updater(self):
        raise NotImplementedError

    def has_voters(self):
        raise NotImplementedError

    def get_voters(self):
        raise NotImplementedError

    def get_comments(self):
        raise NotImplementedError

    def get_attachments(self):
        raise NotImplementedError

    def delete_attachment(self, attachment):
        raise NotImplementedError

    def get_links(self, outward_only=False):
        raise NotImplementedError

    @property
    def events(self):
        raise NotImplementedError

    @property
    def custom_fields(self):
        raise NotImplementedError
