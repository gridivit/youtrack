from xml.dom import Node

from youtrack.helpers import basestring, to_str


class Py3Cmp:
    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0


class YouTrackObject(Py3Cmp):
    def __init__(self, data=None, youtrack=None):
        raise NotImplementedError

    def to_json(self):
        raise NotImplementedError

    def _update_from_attrs(self, el):
        NotImplementedError

    def _update_from_children(self, el):
        NotImplementedError

    @staticmethod
    def _text(el):
        NotImplementedError

    def __repr__(self):
        NotImplementedError

    def __iter__(self):
        NotImplementedError

    def get(self, key, default):
        NotImplementedError

    def __getitem__(self, key):
        NotImplementedError

    def __setitem__(self, key, value):
        NotImplementedError