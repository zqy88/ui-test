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


class DBManagePage(BasePage):

    connectname_prefix="Autotest11_"

    btn_check_connect= "//div[text()='连接测试']"
    btn_menu_1="//span[text()='数据资产管理']"
    btn_menu_2="//span[text()='数据库授权']"
    btn_connect_setting="//div[@class='option']/span"
    btn_dialog_close="//div[@class='manual-dialog']//i"
    btn_add_submit="//div[@class='manual-dialog']//span[text()='确定']"
    btn_add_cancel = "//div[@class='manual-dialog']//span[text()='取消']"
    btn_search = "//span[text()='查询']"
    btn_add_db = "//div[contains(text(),'手动添加')]"
    btn_meta_data="//div[text()='元数据发现设置']"
    btn_add_task="//div[text()='创建任务']"
    btn_add_task_submit="//span[text()='确定并执行']"
    btn_meta_list="//i[@class='el-icon el-icon-arrow-right'] "


    ipt_meta_task="//div[@role='dialog']//input[@placeholder='请选择']"
    ipt_manageway="//input[@placeholder='请选择管理方式']"
    ipt_agentname="//input[@placeholder='请选择agent名称']"
    ipt_connectname="//input[@placeholder='请输入连接名称']"
    ipt_dbname="//input[@placeholder='请选择数据库类型']"
    ipt_ip="//input[@placeholder='请输入IP']"
    ipt_port="//input[@placeholder='请输入端口']"
    ipt_version="//input[@placeholder='请输入版本号']"
    ipt_username="//input[@placeholder='请输入用户名']"
    ipt_pwd="//input[@placeholder='请输入密码']"
    ipt_reponame = "//input[@placeholder='请输入库名']"
    ipt_verifyway = "//input[@placeholder='请选择认证方式']"
    ipt_servername="//input[@placeholder='请输入服务名']"
    ipt_search_connectname = "//input[@placeholder='数据库连接名称搜索']"

    # //label[@for='krb5Conf']/..//input[@placeholder='请选择文件']
    # //label[@for='keytab']/..//input[@placeholder='请选择文件']
    # //input[@placeholder='请输入kerberos服务名']
    # //input[@placeholder='请输入主体']
    # //input[@placeholder='请输入主机名']
    # //span[text()='krb5-hive.conf']
    # //span[text()='admin.keytab']
    # //label[@for='caPem']/..//input[@placeholder='请选择文件']
    # //label[@for='serverPem']/..//input[@placeholder='请选择文件']
    # //div[contains(@style,'position')]//span[text()='server-232.pem']

    ipt_mainbody = "//input[@placeholder='请输入主体']"
    ipt_hostname = "//input[@placeholder='请输入主机名']"
    ipt_kerbservername = "//input[@placeholder='请输入kerberos服务名']"
    ipt_krb5conf = "//label[@for='krb5Conf']/..//input[@placeholder='请选择文件']"
    ipt_keytab = "//label[@for='keytab']/..//input[@placeholder='请选择文件']"
    ipt_capem = "//label[@for='caPem']/..//input[@placeholder='请选择文件']"
    ipt_serverpem = "//label[@for='serverPem']/..//input[@placeholder='请选择文件']"

    opt_manageway_internet="//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='网络']"
    opt_manageway_agent="//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='agent']"
    opt_dbname_mysql="//body/div[@class='el-select-dropdown el-popper']//span[text()='MySQL']"
    opt_verifyway_no="//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='无认证']"
    opt_meta_add_list="//div[contains(@style,'position')]//span[contains(text(),'"+connectname_prefix+"')]"

    search_result_connectname="//span[@class='el-link--inner']"
    search_result_status="//span[@class='set2']"

    message_connect = "//p[contains(@class,'el-message__content')]"

    div_loading="//div[@class='manual-dialog']//div[@class='el-loading-mask']"

    @allure.step("点击大菜单")
    def click_menu_1(self):
        self.click(self.btn_menu_1)


    @allure.step("点击小菜单")
    def click_menu_2(self):
        self.click(self.btn_menu_2)

    @allure.step("点击连接测试")
    def click_test_connect(self):
        self.click(self.btn_check_connect)

    @allure.step("关闭对话框")
    def click_close_dialog(self):
        self.click(self.btn_dialog_close)

    @allure.step("获取回显信息")
    def get_message_connect(self):
        try:
            # WebDriverWait(self.driver, self.sleep_time).until(
            #     EC.element_to_be_clickable((By.XPATH, self.btn_check_connect)))
            WebDriverWait(self.driver, self.sleep_time*6).until(
                    EC.text_to_be_present_in_element_attribute((By.XPATH, self.div_loading),"style","none"))
            sleep(1)
            x=self.get_element(self.message_connect).text
            logger_handler.info(f"连接测试回显状态：{x}")
            return x
            # print(x.text)
        except:
            logger_handler.error(f"INVALID")
            return None
            # print("INVALID")

    @allure.step("进入数据库授权页面")
    def goto_dbmanage_page(self):
        self.click_menu_1()
        self.short_sleep()
        self.click_menu_2()

    def click_add_db(self):
        self.click(self.btn_add_db)

    def click_manageway(self):
        self.click(self.ipt_manageway)

    def click_dbname(self):
        self.click(self.ipt_dbname)

    def click_verifyway(self):
        self.click(self.ipt_verifyway)

    def click_krb5conf(self):
        self.click(self.ipt_krb5conf)

    def click_keytab(self):
        self.click(self.ipt_keytab)

    def click_capem(self):
        self.click(self.ipt_capem)

    def click_serverpem(self):
        self.click(self.ipt_serverpem)

    def click_metadata(self):
        self.click(self.btn_meta_data)

    def click_metalist(self):
        self.click(self.btn_meta_list)

    def click_metaadd(self):
        self.click(self.btn_add_task)

    def clcik_metaadd_submit(self):
        self.click(self.btn_add_task_submit)



    @allure.step("已有所有数据库的连接测试")
    def all_test_connect(self):
        btn_connect = self.get_elements(self.btn_connect_setting)
        for i in btn_connect:
            i.click()
            self.short_sleep()
            self.click_test_connect()
            self.get_message_connect()
            self.click_close_dialog()
            self.short_sleep()

    @allure.step("管理方式选择网络")
    def choose_manageway_internet(self):
        self.click(self.opt_manageway_internet)

    @allure.step("选择数据库名称")
    def choose_dbname(self,dbname):
        loc="//body/div[@class='el-select-dropdown el-popper']//span[text()='"+dbname+"']"
        self.click(loc)

    @allure.step("选择认证方式")
    def choose_verifyway(self,verifyway):
        loc = "//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']//span[text()='"+verifyway+ "']"
        self.click(loc)

    @allure.step("选择krb5conf文件")
    def choose_krb5conf(self, krb5conf):
        loc = "//span[text()='" + krb5conf + "']"
        self.click(loc)

    @allure.step("选择keytab文件")
    def choose_keytab(self, keytab):
        loc = "//span[text()='" + keytab + "']"
        self.click(loc)

    @allure.step("选择capem文件")
    def choose_capem(self, capem):
        loc = "//div[contains(@style,'position')]//span[text()='" + capem + "']"
        self.click(loc)

    @allure.step("选择serverpem文件")
    def choose_serverpem(self, serverpem):
        loc = "//div[contains(@style,'position')]//span[text()='" + serverpem + "']"
        self.click(loc)

    @allure.step("输入连接名称")
    def input_connectname(self, dbname):
        self.input(self.ipt_connectname,self.connectname_prefix+dbname)

    @allure.step("输入ip")
    def input_ip(self, ip):
        self.input(self.ipt_ip,ip)

    @allure.step("输入端口")
    def input_port(self, port):
        self.input(self.ipt_port,port)

    @allure.step("输入用户名")
    def input_username(self, username):
        self.input(self.ipt_username,username)

    @allure.step("输入密码")
    def input_pwd(self, pwd):
        self.input(self.ipt_pwd,pwd)

    @allure.step("输入服务名")
    def input_servername(self,servername):
        self.input(self.ipt_servername,servername)

    @allure.step("输入库名")
    def input_reponame(self, reponame):
        self.input(self.ipt_reponame, reponame)

    @allure.step("输入主体名")
    def input_mainbody(self, mainbody):
        self.input(self.ipt_mainbody, mainbody)

    @allure.step("输入主机名")
    def input_hostname(self, hostname):
        self.input(self.ipt_hostname, hostname)

    @allure.step("输入kerberos服务名")
    def input_kerbservername(self, kerbservername):
        self.input(self.ipt_kerbservername, kerbservername)

    @allure.step("确认添加数据库")
    def click_add_submit(self):
        self.click(self.btn_add_submit)

    @allure.step("取消添加数据库")
    def click_add_cancel(self):
        self.click(self.btn_add_cancel)

    @allure.step("添加数据库")
    def all_add_db(self, dbname, ip, port, username, pwd, reponame, verifyway, servername):
        self.click_add_db()
        self.click_manageway()
        self.choose_manageway_internet()
        self.click_dbname()
        self.choose_dbname(dbname)
        self.input_connectname(dbname)
        self.input_ip(ip)
        self.input_port(port)
        if username != "NONE":self.input_username(username)
        if pwd != "NONE": self.input_pwd(pwd)
        if reponame != "NONE": self.input_reponame(reponame)
        if verifyway != "NONE":
            self.click_verifyway()
            self.choose_verifyway(verifyway)
        if servername != "NONE": self.input_servername(servername)



    @allure.step("通过连接名称查询数据库")
    def input_search_connectname(self, callname):
        self.input(self.ipt_search_connectname, self.connectname_prefix+callname)

    @allure.step("点击查询按钮")
    def click_btn_search(self):
        self.click(self.btn_search)

    @allure.step("获取查询结果的连接名称")
    def get_search_connectname(self):
        try:
            x=self.get_element(self.search_result_connectname)
            logger_handler.info(f"{x.text}")
            return x.text
        except:
            logger_handler.error(f"无法搜索到此数据库")
            return None

    @allure.step("获取查询接口的状态")
    def get_search_status(self):
        try:
            x=self.get_element(self.search_result_status)
            logger_handler.info(f"{x.text}")
            return x.text
        except:
            logger_handler.error(f"无法搜索到此数据库")
            return None

    @allure.step("添加数据库后查询")
    def all_research_post_add(self, callname):
        self.input_search_connectname(callname)
        self.click_btn_search()
        x=self.get_search_connectname()
        y=self.get_search_status()
        return x,y
        # result=0
        # if x == None:
        #     result += 1
        # if y == None:
        #     result += 2
        # if y == "未设置":
        #     result += 4
        # return result

    @allure.step("添加数据库并查询")
    def all_add_and_search(self,callname, dbname, ip, port, username, pwd, reponame, verifyway, servername):
        self.all_add_db_1(callname, dbname, ip, port, username, pwd, reponame, verifyway, servername)
        self.click_connect_and_get()
        self.click_add_submit()
        self.short_sleep()
        r_dbname,r_status = self.all_research_post_add(callname)
        self.assert_equal(r_dbname,self.connectname_prefix+callname)
        self.assert_equal(r_status,"已设置")
        # if result == 0:
        #     logger_handler.info("入库成功")
        #     return 0
        # elif result == 3:
        #     logger_handler.error("添加数据库失败，可能是由于ip或端口重复")
        #     return 1
        # elif result == 4:
        #     logger_handler.error("添加数据库成功，但连接设置为未设置，即无法连接成功")
        #     return 2

    @allure.step("添加数据库并查询")
    def all_add_and_search_special(self,callname, dbname, ip, port, verifyway, capem, serverpem, mainbody, hostname, krb5conf, kerbservername, keytab):
        self.all_add_db_2(callname, dbname, ip, port, verifyway, capem, serverpem, mainbody, hostname, krb5conf, kerbservername, keytab)
        self.click_connect_and_get()
        self.click_add_submit()
        self.short_sleep()
        r_dbname, r_status = self.all_research_post_add(callname)
        self.assert_equal(r_dbname, self.connectname_prefix+callname)
        self.assert_equal(r_status, "已设置")

    def change_default_prefix(self):
        # self.bo=self.bo+1
        self.connectname_prefix="Autotest"+str(self.bo+1)+"_"

    def click_connect_and_get(self):
        self.click_test_connect()
        # self.one_sleep()
        return self.get_message_connect()

    def click_submit_and_get(self):
        self.click_add_submit()
        # self.one_sleep()
        return self.get_message_connect()

    #connecttest(correct\wrongip\wrongport\wrongusername\wrongpwd)
    #           self,callname, dbname, ip, port, username, pwd, reponame, verifyway, servername
    def all_connect_test(self, dbname, ip, port, username, pwd, reponame, verifyway, servername):
        self.all_add_db(dbname, ip, port, username, pwd, reponame, verifyway, servername)
        self.assert_equal(self.click_connect_and_get(), "连接测试成功")
        self.input_port(str(int(port)+1))
        self.short_sleep()
        self.short_sleep()
        self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
        self.input_port(port)
        temp_ip=ip.split('.',3)[0]+"."+ip.split('.',3)[1]+"."+ip.split('.',3)[2]+"."+str(int(ip.split('.',3)[3])+1)
        self.input_ip(temp_ip)
        self.short_sleep()
        self.short_sleep()
        self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
        self.input_ip(ip)
        if username != "NONE":
            self.input_username(username+"_x")
            self.short_sleep()
            self.short_sleep()
            self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
            self.input_username(username)
        if pwd != "NONE":
            self.input_pwd(str(pwd) + "0")
            self.short_sleep()
            self.short_sleep()
            self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
            self.input_pwd(pwd)
        if reponame != "NONE":
            self.input_reponame(reponame + "_x")
            self.short_sleep()
            self.short_sleep()
            self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
            self.input_reponame(reponame)
        if servername != "NONE":
            self.input_servername(servername + "_x")
            self.short_sleep()
            self.short_sleep()
            self.assert_equal(self.click_connect_and_get(), "数据库连接测试失败！！！")
            self.input_servername(servername)
        self.short_sleep()
        self.short_sleep()
        self.assert_equal(self.click_submit_and_get(), "ip和端口重复！无法手动添加！！！")
        # self.input_connectname(dbname+"_x")
        # self.short_sleep()
        # self.short_sleep()
        # self.assert_equal(self.click_submit_and_get(), "ip和端口重复！无法手动添加！！！")
        self.click_add_cancel()
        # self.input_connectname(dbname)
        # self.input_ip(temp_ip)
        # self.short_sleep()
        # self.short_sleep()
        # self.assert_equal(self.click_submit_and_get(), "连接名称重复！无法手动添加！！！")

    @allure.step("添加数据库")
    def all_add_db_1(self,callname, dbname, ip, port, username, pwd, reponame, verifyway, servername):
        self.click_add_db()
        self.click_manageway()
        self.choose_manageway_internet()
        self.click_dbname()
        self.choose_dbname(dbname)
        self.input_connectname(callname)
        self.input_ip(ip)
        self.input_port(port)
        if verifyway != "NONE":
            self.click_verifyway()
            self.choose_verifyway(verifyway)
        if username != "NONE": self.input_username(username)
        if pwd != "NONE": self.input_pwd(pwd)
        if reponame != "NONE": self.input_reponame(reponame)
        if servername != "NONE": self.input_servername(servername)

    @allure.step("添加数据库")
    def all_add_db_2(self, callname, dbname, ip, port, verifyway, capem, serverpem, mainbody, hostname, krb5conf, kerbservername, keytab):
        self.click_add_db()
        self.click_manageway()
        self.choose_manageway_internet()
        self.click_dbname()
        self.choose_dbname(dbname)
        self.input_connectname(callname)
        self.input_ip(ip)
        self.input_port(port)
        if verifyway != "NONE":
            self.click_verifyway()
            self.choose_verifyway(verifyway)
        if capem != "NONE":
            self.click_capem()
            self.choose_capem(capem)
        if krb5conf != "NONE":
            self.click_krb5conf()
            self.choose_krb5conf(krb5conf)
        if keytab != "NONE":
            self.click_keytab()
            self.choose_keytab(keytab)
        if mainbody != "NONE":
            self.input_mainbody(mainbody)
        if hostname != "NONE":
            self.input_hostname(hostname)
        if kerbservername != "NONE":
            self.input_kerbservername(kerbservername)
        if serverpem != "NONE":
            self.click_serverpem()
            self.choose_serverpem(serverpem)

    def assert_connect_corrcet(self,callname, dbname, ip, port, username, pwd, reponame, verifyway, servername):
        self.all_add_db_1(callname, dbname, ip, port, username, pwd, reponame, verifyway, servername)
        self.one_sleep()
        self.assert_equal(self.click_connect_and_get(), "连接测试成功")
        self.click_add_cancel()

    def assert_connect_corrcet_special(self,callname, dbname, ip, port, verifyway, capem, serverpem, mainbody, hostname, krb5conf, kerbservername, keytab):
        self.all_add_db_2(callname, dbname, ip, port, verifyway, capem, serverpem, mainbody, hostname, krb5conf, kerbservername, keytab)
        self.one_sleep()
        self.assert_equal(self.click_connect_and_get(), "连接测试成功")
        self.click_add_cancel()





if __name__=="__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.all_login()
    dbmp=DBManagePage(driver)
    dbmp.goto_dbmanage_page()
    dbmp.long_sleep()

