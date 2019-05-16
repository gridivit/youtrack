from youtrack.youtrack_types.bundle_element import BundleElement


class VersionField(BundleElement):
    def __init__(self, data=None, youtrack=None):
        super().__init__("version", data, youtrack)

    def _update_specific_attributes(self, xml):
        raise NotImplementedError
