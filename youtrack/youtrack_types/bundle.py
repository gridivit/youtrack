
from xml.sax.saxutils import escape

from youtrack.youtrack_types.youtrack_object import YouTrackObject


class Bundle(YouTrackObject):
    def __init__(self, element_tag_name, bundle_tag_name, data=None, youtrack=None):
        self._element_tag_name = element_tag_name
        self._bundle_tag_name = bundle_tag_name
        self.values = []
        super().__init__(data, youtrack)

    def _update(self, xml):
        raise NotImplementedError

    def to_json(self):
        raise NotImplementedError

    def get_field_type(self):
        return self._element_tag_name

    def create_element(self, name):
        element = self._create_element(None)
        element.name = name
        return element

    def _create_element(self, json):
        raise NotImplementedError
