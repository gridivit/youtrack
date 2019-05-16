from youtrack.youtrack_types.bundle import Bundle
from youtrack.youtrack_types.owned_field import OwnedField


class OwnedFieldBundle(Bundle):
    def __init__(self, json=None, youtrack=None):
        super().__init__("ownedField", "ownedFieldBundle", json, youtrack)

    def _create_element(self, xml):
        raise NotImplementedError
