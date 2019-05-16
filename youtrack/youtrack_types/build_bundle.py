from youtrack.youtrack_types.bundle import Bundle
from youtrack.youtrack_types.build import Build


class BuildBundle(Bundle):
    def __init__(self, data=None, youtrack=None):
        super().__init__("build", "buildBundle", data, youtrack)

    def _create_element(self, xml):
        raise NotImplementedError
