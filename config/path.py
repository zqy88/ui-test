import os

# 当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# config目录
config_dir = os.path.dirname(current_file_path)

# 项目目录---工程目录命名为root_dir
root_dir = os.path.dirname(config_dir)

# ini配置文件的路径
ini_path = os.path.join(config_dir, 'config.ini')

# 日志文件路径
log_dir = os.path.join(root_dir, 'log')
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# 测试报告目录
report_dir = os.path.join(root_dir,'report')
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 验证码图片目录
verify_img_dir = os.path.join(root_dir, 'verify_img')
if not os.path.exists(verify_img_dir):
    os.mkdir(verify_img_dir)

# 截图文件路径
img_dir = os.path.join(root_dir, 'image')
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

# 测试数据的目录
data_dir = os.path.join(root_dir, 'data')

# # yaml配置文件路径
# yaml_path = os.path.join(config_dir, 'config.yaml')
#
# # bps报文的目录
# pcap_dir = os.path.join(root_dir, 'pcap')
#
# # 保存所有注册成功的手机号
# registered_num_path = os.path.join(data_dir, 'registered_nums.txt')

