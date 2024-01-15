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
from common.logger_handler import logger_handler
from selenium.common import exceptions
from datetime import datetime
import allure
from config import path


class BasePage():

    sleep_time = 10
    connectname_prefix = "Autotest11_"


    def __init__(self, driver):
        self.driver = driver

    def goto_url(self, url: str):
        """
        访问url页面
        :param url：字符串类型，访问的网页地址，可以是绝对地址、相对地址
        """
        self.driver.get(url)
        logger_handler.info(f"访问网页：{url}")

        # if url.startswith('http'):
        #     self.driver.get(url)
        # else:
        #     url = self.host + url
        #     self.driver.get(url)
        # logger_handler.info(f"访问网页：{url}")

    def click(self, locator, force=False):
        # WebDriverWait(self.driver, self.sleep_time).until(
        #     EC.presence_of_element_located((By.XPATH, locator)))
        # self.driver.find_element(By.XPATH, locator).click()
        #
        try:
            WebDriverWait(self.driver, self.sleep_time).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            elem = self.driver.find_element(By.XPATH, locator)
            if not force:
                self.driver.execute_script("arguments[0].click()", elem)
            else:
                self.driver.execute_script("arguments[0].click({force:true})", elem)
            logger_handler.info(f"单击元素：{locator}")
            return self
        except exceptions.NoSuchElementException as e:
            logger_handler.error(f"元素无法定位，鼠标单击失败：{locator}")

    def clear(self, locator):
        try:
            WebDriverWait(self.driver, self.sleep_time).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            self.driver.find_element(By.XPATH, locator).send_keys(Keys.CONTROL, "a")
            self.driver.find_element(By.XPATH, locator).send_keys(Keys.DELETE)
            logger_handler.info(f"元素内容被清空：{locator}")
        except exceptions.NoSuchElementException as e:
            logger_handler.error(f"元素无法定位：{locator}")

    def input(self, locator, value):
        try:
            WebDriverWait(self.driver, self.sleep_time).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            self.clear(locator)
            self.driver.find_element(By.XPATH, locator).send_keys(value)
            logger_handler.info(f"元素被输入内容：{locator}")
        except exceptions.NoSuchElementException as e:
            logger_handler.error(f"元素无法定位，输入内容失败：{locator}")

    def long_sleep(self):
        sleep(self.sleep_time*20)
        logger_handler.info(f"长睡")

    def short_sleep(self):
        sleep(self.sleep_time/5)
        logger_handler.info(f"小睡")

    def one_sleep(self):
        sleep(1)
        logger_handler.info(f"睡1s")

    def get_element(self, locator):
        try:
            WebDriverWait(self.driver, self.sleep_time).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            logger_handler.info(f'元素定位成功：{locator}')
            return self.driver.find_element(By.XPATH, locator)
        except exceptions.NoSuchElementException as e:
            logger_handler.error(f'元素无法定位：{locator}')


    def get_elements(self, locator):
        try:
            WebDriverWait(self.driver, self.sleep_time).until(
                EC.presence_of_element_located((By.XPATH, locator)))
            logger_handler.info(f'元素定位成功：{locator}')
            return self.driver.find_elements(By.XPATH, locator)
        except exceptions.NoSuchElementException as e:
            logger_handler.error(f'元素无法定位：{locator}')

    def base64_to_img_file(self,base64_str, file_path):
        """
        将Base64字符串转化为图片并保存在本地
        :param base64_str:原始base64字符串
        :param file_path:本地文件的路径
        :return:
        """
        str1 = re.sub(r'%0A', "\\n", base64_str)
        str2 = re.sub(r'data:image/png;base64,', '', str1)
        imgdata = base64.b64decode(str2)
        file = open(file_path, 'wb')
        file.write(imgdata)
        file.close()


    def get_distance_block_left_to_canvas_left(self,canvas_img_path, block_img_path):
        """
        获取验证码背景图中缺口最左边到背景图最左边的距离
        :param canvas_img_path:背景图片的路径
        :param block_img_path: 滑块图片的路径
        :return:返回背景图中缺口最左边到背景图最左边的距离
        """
        # 以灰度模式加载背景图
        canvas_gray = cv2.imread(canvas_img_path, 0)
        # 以灰度模式加载滑块图片
        block_gray = cv2.imread(block_img_path, 0)
        # 匹配小图在大图中的位置-匹配模式
        res = cv2.matchTemplate(canvas_gray, block_gray, cv2.TM_CCORR_NORMED)
        # 匹配背景图中缺口最左边到背景图最左边边缘的结果
        value = cv2.minMaxLoc(res)
        print(value)
        # 大图中缺口最左边到大图最左边的距离
        x = value[2][0]
        print(f"图库计算出的初始滑动距离为:{x}")
        return x

    def get_actual_slide_dis(self,match_dis):
        """
        因为ismc滑动的是下方滑块，不是缺口图片，经过手工测试，发现两者的滑动距离有误差，需要将这个误差计算在
        实际要滑动的距离中，该误差也是按比例算的，也不一定准，可以不停调试，直到最佳结果
        :param match_dis:背景图片和缺口图片匹配配置的x坐标
        :return:滑块误差+x坐标得到的实际要滑动的值，这个值其实也还是会不准
        """
        # 这里的120是手工测计算得到的，调试发现像素在120以内误差小些（120时误差为10，所以按比例计算）；
        # 大于120时无法大些，分段计算
        # 其实都是经验值，也不是很准，分支分的越多会越准
        if match_dis < 120:
            error = int(match_dis * 10 / 120)
        else:
            error = int(10 + (match_dis - 120) * 6 / 160)
        actual_dis = match_dis + error
        return actual_dis

    def get_tracks(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance:偏移量
        :return:移动轨迹
        """
        # 移动轨迹
        tracks = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 5
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            tracks.append(round(move))
        return tracks

    def screenshot(self):
        """
        截图，并保存在本地img目录中
        :return:
        """
        current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        filename = f'{current_time}.png'
        filepath = os.path.join(path.img_dir, filename)
        self.driver.get_screenshot_as_file(filepath)
        logger_handler.info(f'完成屏幕截图，图片文件名为{filepath}')
        return self

    def add_screenshot_to_allure_report(self):
        """
        在allure测试报告中附加截图
        :return:
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name='测试结果截图',
            attachment_type='png'
        )
        logger_handler.info("在测试报告中附加截图")
        return self

    @allure.step('断言实际值与预期值是否一致')
    def assert_equal(self, actual_value, expected_value):
        """
        判断预期值与实际值是否相等
        :param actual_value:
        :param expected_value:
        :return:
        """
        try:
            assert actual_value == expected_value
            print(actual_value, expected_value)
            logger_handler.info("断言成功")
        except AssertionError as e:
            logger_handler.error("断言失败")
            self.screenshot()
            self.add_screenshot_to_allure_report()
            raise e

    @allure.step('断言某元素是否存在')
    def assert_exist_elem(self, loc_elem):
        """
        根据元素定位判断某元素是否存在
        :param loc_elem: 元素定位元组
        :return:
        """
        try:
            assert self.get_element(loc_elem)
            logger_handler.info("断言成功")
        except AssertionError as e:
            logger_handler.error("断言失败")
            self.screenshot()
            self.add_screenshot_to_allure_report()
            raise e

    @allure.step('断言表达式')
    def assert_exp(self, exp):
        try:
            assert exp
            logger_handler.info("断言成功")
        except AssertionError as e:
            logger_handler.error("断言失败")
            self.screenshot()
            self.add_screenshot_to_allure_report()
            raise e
