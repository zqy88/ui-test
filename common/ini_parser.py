from configparser import ConfigParser
from config.path import ini_path


class IniConfigParser(ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(ini_path, encoding='utf-8')


ini_parser = IniConfigParser()

if __name__ == '__main__':
    name = ini_parser.get('logger', 'name')
    level = ini_parser.get('logger', 'level')
    print(name, level)
