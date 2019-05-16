from youtrack.youtrack_types.bundle_element import BundleElement


class EnumField(BundleElement):
    def __init__(self, data=None, youtrack=None):
        super().__init__("value", data, youtrack)
