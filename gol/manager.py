import time
import yaml

from gol.constants import *


class Manager:

    def __init__(self, config: dict):
        self.file = config['file']      # Chronolog file path.

    @staticmethod
    def try_get_config() -> (bool, dict):
        """
        Load gol config if local or global config exists.

        :return: True/False config loaded, config.
        """

        if os.path.exists(LOCAL_CONFIG_PATH):
            return True, yaml.load(open(LOCAL_CONFIG_PATH, 'r'))
        elif os.path.exists(GLOBAL_CONFIG_PATH):
            return True, yaml.load(open(GLOBAL_CONFIG_PATH, 'r'))
        else:
            print('No gol config found!\nCreate %s or %s or call \'gol init\''
                  % (LOCAL_CONFIG_PATH, GLOBAL_CONFIG_PATH))
            return False, None

    @staticmethod
    def _today_head() -> str:
        head = time.strftime('\n## %Y-%m-%d\n')
        return head

    @staticmethod
    def _current_activity() -> str:
        act = time.strftime('* %H.%M:')
        return act

    def add_to_begin(self, text: str):
        with open(self.file, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(text + content)

    def add_today_head(self):
        head = self._today_head()
        self.add_to_begin(head)

    def add_activity(self, description: str):
        act = self._current_activity()
        self.add_to_begin('%s %s\n' % (act, description))
