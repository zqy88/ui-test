import allure
import os
from config import path
from common.logger_handler import logger_handler
from datetime import datetime


def get_current_time():
    """
    获取当前时间
    :return:当前时间，时间格式为YYYY-MM-DD-HH-MM-SS
    """
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def generate_allure_report():
    """
    生成allure测试报告，测试报告名为当前时间分，统一存放在report目录中。
    :return:
    """
    sub_allure_report_dir = os.path.join(path.report_dir, get_current_time())
    ret = os.system(f'allure generate ./allure_files -o {sub_allure_report_dir}')
    if ret:
        logger_handler.error('生成测试报告失败')
    else:
        logger_handler.info(f'生成测试报告成功，报告目录为{sub_allure_report_dir}')








