from youtrack.youtrack_types.bundle import Bundle
from youtrack.youtrack_types.version_field import VersionField


class VersionBundle(Bundle):
    def __init__(self, data=None, youtrack=None):
        super().__init__("version", "versions", data, youtrack)

    def _create_element(self, xml):
        return VersionField(xml, self.youtrack)