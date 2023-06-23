class Session:
    def __init__(self):
        self._current_user = None

    def set_current_user(self, user):
        self._current_user = user

    def get_current_user(self):
        return self._current_user
