#!/usr/bin/python3
import requests
import logging

logging.basicConfig(	# 输出到Terminal的基本设置
    format="%(levelname)-8s %(asctime)s (%(filename)-15s: line %(lineno)3d): %(message)s",
    level=logging.INFO,
    filename='buptnet.log'
)

Getway_IP = "http://10.3.8.211/login"  # 校园网网关登录地址 或换成"http://gw.bupt.edu.cn/login"
LogOut_URL = "http://10.3.8.211/logout"  # 校园网网关登出地址 或换成"http://gw.bupt.edu.cn/logout"
Check_URL = "http://www.baidu.com"  # 用以检测是否可以连接到外网
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
username = "2019?????"  # 请改成自己的学工号
password = "Abc??????"  # 请改成自己的校园网密码


def check_network():
    # 必须禁止重定向，否则 status_code 一直是 200
    res = requests.get(Check_URL, timeout=1, allow_redirects=False)
    logging.debug(res.status_code)
    logging.debug(res.text)
    if res.status_code == 200:
        logging.debug('您已经成功登录。')
        return True
    else:
        logging.debug('未登录。')
        return False


def login(username, password):
    params = {
        'user': username,
        'pass': password
    }
    res = requests.post(Getway_IP, headers=headers, params=params)
    logging.debug(res.text)
    return res


def logout():
    res = requests.get(LogOut_URL, headers=headers, allow_redirects=False)
    logging.debug(res.text)
    return res


def main():
    if check_network():
        logging.info("您已经登录过！")
    else:
        login(username, password)
        if check_network():
            logging.info("登录成功！")
        else:
            logging.error("登录失败，请检查账号密码！")

if __name__ =="__main__":
    main()


# # 测试登出
# if logout().status_code == 302: # 登出后会重定向
#     logging.info("登出成功！")
# else:
#     logging.error("登出失败！")
# # 检查一下网络看看是否确实登出
# if check_network():
#     logging.error("确实登出失败！")
# else:
#     logging.info("确实登出成功！")
