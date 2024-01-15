from page.basepage import BasePage
from common.logger_handler import logger_handler
from selenium.common import exceptions
import pytest
import allure
from page.basepage import BasePage
from selenium import webdriver
import base64

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from time import sleep
import random
import os
import re
import cv2
from page.login_page import LoginPage


class MenuPage(BasePage):
    menu_data = [['"数据资产概览"', '"数据资产地图"', '"数据库连接统计"'],
                 ["'数据资产管理'", '"数据库授权"', '"数据库列表"'], ['数据资产管理', '文件系统授权', '文件服务器列表'],
                 ['"数据资产管理"', '"业务系统管理"', '"业务系统列表"']
                 ]

    @allure.step("点击大菜单")
    def click_big_menu(self, big_menu):
        loc="//span[text()="+big_menu+"]"
        print(loc)
        self.click(loc)

    @allure.step("点击小菜单")
    def click_small_menu(self, small_menu):
        loc = "//span[text()=" + small_menu + "]"
        self.click(loc)

    @allure.step("检查页面是否正确")
    def check_page(self, check_text):
        loc = "//div[contains(text(),"+check_text+")]"
        self.assert_exist_elem(loc)
        # try:
        #     self.get_element(loc)
        #     logger_handler.info(f'页面加载成功')
        #     return True
        # except exceptions.TimeoutException as e:
        #     logger_handler.error(f'页面加载失败')
        #     return False

    # @pytest.mark.parametrize("big_menu,small_menu,check_text",menu_data)
    @allure.step("页面跳转并检查")
    def check_all_page(self, big_menu, small_menu, check_text):
        self.click_big_menu(big_menu)
        self.short_sleep()
        self.click_small_menu(small_menu)
        self.check_page(check_text)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.all_login()
    mp = MenuPage(driver)
    mp.check_all_page(mp.menu_data[1][0], mp.menu_data[1][1], mp.menu_data[1][2])
    mp.long_sleep()
