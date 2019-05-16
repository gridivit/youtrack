from youtrack.youtrack_types.bundle_element import BundleElement


class StateField(BundleElement):
    def __init__(self, json=None, youtrack=None):
        super().__init__("state", json, youtrack)

    def _update_specific_attributes(self, data):
        raise NotImplementedError