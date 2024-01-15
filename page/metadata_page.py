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
from common.logger_handler import logger_handler
import allure


class MetaDataPage(BasePage):

    connectname_prefix="Autotest11_"

    btn_db_data="//div[text()='数据库管理']"
    btn_meta_data="//div[text()='元数据发现设置']"
    btn_add_task="//div[text()='创建任务']"
    btn_add_task_submit="//span[text()='确定并执行']"
    btn_meta_list="//i[@class='el-icon el-icon-arrow-right']"
    btn_meta_list_check="//span[text()='查看']"

    btn_menu_1="//span[text()='数据资产管理']"
    btn_menu_2="//span[text()='数据库授权']"


    ipt_meta_task="//label[text()='扫描对象']/..//input"

    opt_meta_add_list="//div[contains(@style,'position')]//span[contains(text(),'"+connectname_prefix+"')]"

    search_result_status="//div[text()='已完成']"
    search_result_table="//tbody//tr"

    message_connect = "//p[contains(@class,'el-message__content')]"

    div_loading="//div[@class='manual-dialog']//div[@class='el-loading-mask']"

    @allure.step("点击大菜单")
    def click_menu_1(self):
        self.click(self.btn_menu_1)

    @allure.step("点击小菜单")
    def click_menu_2(self):
        self.click(self.btn_menu_2)

    @allure.step("点击元数据发现设置页面")
    def click_metadata(self):
        self.click(self.btn_meta_data)

    @allure.step("点击数据库管理页面")
    def click_dbdata(self):
        self.click(self.btn_db_data)

    @allure.step("点击创建任务按钮")
    def click_metaadd(self):
        self.click(self.btn_add_task)

    @allure.step("点击扫描对象输入框")
    def click_scanobject(self):
        self.click(self.ipt_meta_task)

    @allure.step("选择扫描对象")
    def choose_scanobject(self,callname):
        self.click("//div[contains(@style,'position')]//span[contains(text(),'"+self.connectname_prefix+callname+"')]")

    @allure.step("点击提交任务")
    def click_metaadd_submit(self):
        self.click(self.btn_add_task_submit)

    @allure.step("点击第一个任务")
    def click_metalist(self):
        self.click(self.btn_meta_list)

    @allure.step("查看任务")
    def click_metalist_check(self):
        self.click(self.btn_meta_list_check)

    def get_metadate_status(self):
        for i in range(30):
            try:
                self.click_dbdata()
                self.short_sleep()
                self.click_metadata()
                self.short_sleep()
                self.click_metalist()
                WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, self.search_result_status)))
                elem = self.driver.find_element(By.XPATH, self.search_result_status)
                return elem.text
            except:
                continue
        return None


    def get_metadate_table(self):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.search_result_table)))
            return True
        except:
            return False

    @allure.step("进入元数据发现页面")
    def goto_metadata_page(self):
        self.click_menu_1()
        self.short_sleep()
        self.click_menu_2()
        self.short_sleep()
        self.click_metadata()

    @allure.step("创建元数据发现任务")
    def add_metadata_task(self,callname):
        self.click_metaadd()
        self.short_sleep()
        self.click_scanobject()
        self.short_sleep()
        self.choose_scanobject(callname)
        self.short_sleep()
        self.click_scanobject()
        self.short_sleep()
        self.click_metaadd_submit()
        self.short_sleep()
        self.assert_equal(self.get_metadate_status(),"已完成")
        self.click_metalist_check()
        self.short_sleep()
        self.assert_equal(self.get_metadate_table(),True)









if __name__=="__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.all_login()
    mdp=MetaDataPage(driver)
    mdp.goto_metadata_page()
    mdp.short_sleep()
    mdp.add_metadata_task()
    mdp.long_sleep()

