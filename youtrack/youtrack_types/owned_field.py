from youtrack.youtrack_types.bundle_element import BundleElement


class OwnedField(BundleElement):
    def __init__(self, data=None, youtrack=None):
        super().__init__("ownedField", data, youtrack)

    def _update_specific_attributes(self, xml):
        owner = xml.getAttribute("owner")
        if owner != '<no user>':
            self.owner = owner
        else:
            self.owner = None
