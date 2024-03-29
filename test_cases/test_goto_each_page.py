# import pytest
# from test_cases.conftest import *
# from page.DBManage_page import DBManagePage
# from page.menu_page import MenuPage
# import allure
#
# menu_data = [['"数据资产概览"', '"数据资产地图"', '"数据库连接统计"'],
#              ["'数据资产管理'", '"数据库授权"', '"数据库列表"'], ['"数据资产管理"', '"文件系统授权"', '"文件服务器列表"'],['"数据资产管理"', '"业务系统管理"', '"业务系统列表"'],
#              ['"数据分类分级"','"分类分级列表"','"数据分类分级列表"'],['"数据分类分级"','"分类分级任务"','"分类分级任务列表"'],['"数据分类分级"','"分类分级模板"','"分类分级模板库"'],
#              ['"敏感数据发现"','"敏感数据分布"','"敏感数据表"'],['"敏感数据发现"','"敏感文件分布"','"涉敏文件列表"'],['"敏感数据发现"','"敏感数据扫描"','"任务列表"'],['"敏感数据发现"','"敏感文件扫描"','"任务列表"'],
#              ['"流量异常监测"','"异常行为监测"','"异常行为列表"'],['"流量异常监测"','"异常行为策略"','"异常行为策略列表"'],
#              ['"安全风险核查"','"API接口风险"','"API接口风险列表"'],['"安全风险核查"','"弱口令"','"资产弱口令列表"'],['"安全风险核查"','"不合规配置"','"资产不合规配置列表"'],['"安全风险核查"','"资产漏洞"','"资产漏洞列表"'],
#              ['"数据库审计"','"操作日志"','"操作日志列表"'],['"数据库审计"','"审计事件"','"审计事件列表"'],['"数据库审计"','"审计策略"','"审计策略列表"'],
#              ['"数据跨境专题"','"跨境数据图谱"','"跨境数据传输国家统计"'],['"数据跨境专题"','"跨境资产分析"','"资产数据管理列表"'],['"数据跨境专题"','"跨境流转监测"','"跨境流转监测管理"'],['"数据跨境专题"','"跨境白名单"','"跨境白名单管理"'],
#              ['"配置管理"','"敏感标签管理"','"敏感标签管理"'],
#              ['"数据风险评估"','"数据资产报告"','"数据资产报告列表"'],['"数据风险评估"','"数据风险报告"','"数据风险报告列表"'],['"数据风险评估"','"数据评估报告"','"数据评估报告列表"'],
#              ['"数据安全报告"','"数据安全综合报告"','"数据安全报告列表"'],
#              ['"系统管理"','"系统概况"','"内存信息"'],['"系统管理"','"Agent管理"','"Agent列表"'],['"系统管理"','"用户管理"','"用户列表"'],['"系统管理"','"角色权限"','"角色列表"'],['"系统管理"','"操作日志"','"操作日志列表"'],
#              ]
#
#
# # def test_2():
# #     mp.short_sleep()
# #     assert mp.check_all_page(menu_data[1][0], menu_data[1][1], menu_data[1][2])==True
#
#
# @pytest.mark.parametrize("big_menu,small_menu,check_text", menu_data)
# @allure.step
# def test_1(big_menu, small_menu, check_text):
#     mp.check_all_page(big_menu, small_menu, check_text)
