from youtrack.youtrack_types.bundle_element import BundleElement


class Build(BundleElement):
    def __init__(self, data=None, youtrack=None):
        super().__init__("build", data, youtrack)

    def _update_specific_attributes(self, json):
        raise NotImplementedError
