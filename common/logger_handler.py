import os
import logging
from logging import Logger
from datetime import datetime
from config.path import log_dir
from common.ini_parser import ini_parser

# 读取ini配置文件中logger收集器的name和level
logger_name = ini_parser.get('logger', 'name')
logger_level = ini_parser.get('logger', 'level')


class MyLoggerHandler(Logger):
    def __init__(self):
        super().__init__(logger_name, logger_level)

        # 设置日志格式
        format_str = '%(asctime)s %(name)s %(filename)s %(lineno)d %(levelname)s : %(message)s'
        # 实例化格式对象
        log_formatter = logging.Formatter(format_str)

        # 实例化输出渠道-控制台
        console_handler = logging.StreamHandler()
        # 实例化输出渠道-文件
        current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name = f'{current_time}.log'
        file_path = os.path.join(log_dir, file_name)
        file_handler = logging.FileHandler(file_path, encoding="utf-8")

        # 输出渠道设置日志格式
        console_handler.setFormatter(log_formatter)
        file_handler.setFormatter(log_formatter)

        # 日志收集器绑定输出渠道
        self.addHandler(console_handler)
        self.addHandler(file_handler)


# 实例化一个日志处理器
logger_handler = MyLoggerHandler()

if __name__ == '__main__':
    logger_handler.debug('debug调试')
    logger_handler.info('info信息')
    logger_handler.warning('waring警告')
    logger_handler.error('error错误')
    logger_handler.critical('critical致命错误')
