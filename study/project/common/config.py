from configparser import ConfigParser
import os
from study.project.common.constant import CONF_DIR

class MyConfig(ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(filenames=os.path.join(CONF_DIR, 'conf.ini'), encoding='utf8')


my_config = MyConfig()