from youtrack.youtrack_types.bundle import Bundle
from youtrack.youtrack_types.state_field import StateField


class StateBundle(Bundle):
    def __init__(self, data=None, youtrack=None):
        super().__init__("state", "stateBundle", data, youtrack)

    def _create_element(self, data):
        raise NotImplementedError