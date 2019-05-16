from xml.dom import Node

from xml.sax.saxutils import escape

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class BundleElement(YouTrackObject):
    def __init__(self, element_tag_name, data=None, youtrack=None):
        self.element_name = element_tag_name
        super().__init__(data, youtrack)

    def to_json(self):
        raise NotImplementedError

    def _update(self, xml):
        raise NotImplementedError

    def _update_specific_attributes(self, xml):
        raise NotImplementedError
