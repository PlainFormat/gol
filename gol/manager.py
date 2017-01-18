import time


class Manager:

    def __init__(self, filename: str):
        self.filename = filename

    @staticmethod
    def _today_head() -> str:
        head = time.strftime('\n## %Y-%m-%d\n')
        return head

    @staticmethod
    def _current_activity() -> str:
        act = time.strftime('* %H.%M:')
        return act

    def add_to_begin(self, text: str):
        with open(self.filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(text + content)

    def add_today_head(self):
        head = self._today_head()
        self.add_to_begin(head)

    def add_activity(self, description: str):
        act = self._current_activity()
        self.add_to_begin('%s %s\n' % (act, description))
