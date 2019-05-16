from youtrack.youtrack_types.bundle import Bundle
from youtrack.youtrack_types.enum_field import EnumField


class EnumBundle(Bundle):
    def __init__(self, data=None, youtrack=None):
        super().__init__("value", "enumeration", data, youtrack)

    def _create_element(self, json):
        raise NotImplementedError

    def get_field_type(self):
        return "enum"
